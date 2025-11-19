import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Gokul", "Rahul", "Arun"],
    "Age": [21, 22, 20],
    "Score": [88, 92, 77]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Selecting a single column
print("\nNames Column:\n", df["Name"])

# Selecting multiple columns
print("\nName & Score:\n", df[["Name", "Score"]])

# Adding a new column
df["Pass"] = df["Score"] >= 80
print("\nDataFrame with new column:\n", df)

# Basic statistics
print("\nAverage Score:", df["Score"].mean())
