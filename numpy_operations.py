import numpy as np

# Creating NumPy arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Basic math operations
print("\nAddition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# Array statistics
print("\nMean:", arr1.mean())
print("Maximum:", arr1.max())
print("Minimum:", arr1.min())

# Reshaping
matrix = arr1.reshape(2, 2)
print("\nReshaped Matrix:\n", matrix)
