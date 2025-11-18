import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
print("\nA + B:\n", A + B)

# Matrix multiplication
print("\nA * B (element-wise):\n", A * B)

# Dot product
print("\nDot Product A @ B:\n", A @ B)

# Transpose
print("\nTranspose of A:\n", A.T)
