#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:00:59
#SBATCH --output=file.out
#SBATCH -A anakano_429

mpirun -n $SLURM_NTASKS ./ZetaSum
mpirun -n             2 ./ZetaSum
mpirun -n             4 ./ZetaSum
mpirun -n             1 ./ZetaSum