import numpy as np

# Create a numpy array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Basic operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# Reshaping arrays
matrix = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print("Matrix:\n", matrix)

# Element-wise operations
print("Matrix + 10:\n", matrix + 10)
print("Matrix * 2:\n", matrix * 2)
