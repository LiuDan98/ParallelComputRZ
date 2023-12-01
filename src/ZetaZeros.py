import mpmath
import matplotlib.pyplot as plt

# Set mpmath to use higher precision (adjust as needed)
mpmath.mp.dps = 30

# Number of zeros to compute
num_zeros = 1000

# Compute and store the nontrivial zeros of the Riemann zeta function
zero_points = [mpmath.zetazero(n) for n in range(1, num_zeros + 1)]

# Print the zero points
for i, zero_point in enumerate(zero_points):
    print(f"Zero Point {i + 1}: {zero_point}")

# Plot the zeros in the complex plane
real_parts = [mpmath.re(z) for z in zero_points]
imag_parts = [mpmath.im(z) for z in zero_points]

plt.scatter(real_parts, imag_parts, color='red')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Distribution of Riemann Zeta Function Zeros')
plt.grid(True)
plt.show()
