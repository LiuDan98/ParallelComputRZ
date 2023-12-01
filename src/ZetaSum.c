#include <stdio.h>
#include <math.h>
#include <mpi.h>

#define EXPECTED_RESULT 1.202056903159594
#define S 3

int main(int argc, char *argv[]) {
    FILE *file;
    int Rank, NumberOfProcess, n, i, INFINITE;
    long double sum = 0, sharedSum = 0, tempSum = 0;
    long double StartParallelTime = 0, EndParallelTime = 0;
    long double startSerialTime = 0, endSerialTime = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &NumberOfProcess);
    MPI_Comm_rank(MPI_COMM_WORLD, &Rank);

    int arr[NumberOfProcess];
    int NumberOfIterationPerProcess = 0;

    if (Rank == 0) {
        INFINITE = 100;
        file = fopen("ZetaSum.txt", "a");
        fprintf(file, "p=%d\t\t", NumberOfProcess);
        fprintf(file, "n=%d\t\t", INFINITE);

        startSerialTime = MPI_Wtime();
        NumberOfIterationPerProcess = INFINITE / NumberOfProcess;

        if (NumberOfProcess == 1) {
            arr[0] = INFINITE;
        } else {
            for (i = 0; i < NumberOfProcess - 1; i++) {
                arr[i] = NumberOfIterationPerProcess;
                sum += arr[i];
            }
            arr[NumberOfProcess - 1] = INFINITE - sum;
        }
        endSerialTime = MPI_Wtime();
    }

    MPI_Bcast(&INFINITE, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&sharedSum, 1, MPI_LONG_DOUBLE, 0, MPI_COMM_WORLD);
    MPI_Bcast(&arr, NumberOfProcess, MPI_INT, 0, MPI_COMM_WORLD);

    int start = Rank * NumberOfIterationPerProcess + 1;
    int end = (Rank + 1) * NumberOfIterationPerProcess;

    if (Rank + 1 == NumberOfProcess) {
        start = Rank * NumberOfIterationPerProcess + 1;
        end = INFINITE;
    }

    StartParallelTime = MPI_Wtime();

    for (n = start; n <= end; n++) {
        tempSum += (1.0L / pow(n, S));
    }

    MPI_Reduce(&tempSum, &sharedSum, 1, MPI_LONG_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    EndParallelTime = MPI_Wtime();

    if (Rank == 0) {
        long double Tserial = endSerialTime - startSerialTime;
        long double Tparallel = EndParallelTime - StartParallelTime;
        long double SpeedUp = Tserial / Tparallel;
        long double Efficiency = SpeedUp / NumberOfProcess;

        printf("Sum= %0.15Lf ", sharedSum);
        fprintf(file, "sum=%0.15Lf\t\t", sharedSum);

        printf("Error= %0.15Lf\n", EXPECTED_RESULT - sharedSum);
        fprintf(file, "Error=%0.15Lf\t\t", EXPECTED_RESULT - sharedSum);

        printf("Efficiency= %0.15Lf seconds\n", Efficiency);
        fprintf(file, "Efficiency=%0.15Lf\n", Efficiency);

        fclose(file);
    }

    MPI_Finalize();
    return 0;
}
