import pandas as pd

# Reading CSV file
df = pd.read_csv("sample.csv")

print("Data Loaded:\n", df)

# Display shape
print("\nShape:", df.shape)

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Sorting
sorted_df = df.sort_values(by="Age")
print("\nSorted by Age:\n", sorted_df)
