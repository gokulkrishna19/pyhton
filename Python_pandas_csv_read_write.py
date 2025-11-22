import pandas as pd

# Create DataFrame
data = {
    "Student": ["Aju", "Riya", "Rahul"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print("Created DataFrame:\n", df)

# Save to CSV
df.to_csv("students.csv", index=False)
print("\nSaved to students.csv")

# Read CSV
df2 = pd.read_csv("students.csv")
print("\nRead from CSV:\n", df2)
