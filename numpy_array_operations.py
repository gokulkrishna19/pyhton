import numpy as np

arr = np.array([10, 20, 30, 40])

# Element-wise operations
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Square:", arr ** 2)

# Reshape
reshaped = arr.reshape(2, 2)
print("\nReshaped Matrix:\n", reshaped)

# Concatenate
arr2 = np.array([50, 60])
print("\nConcatenated:", np.concatenate([arr, arr2]))
