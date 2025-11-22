import pandas as pd

# Sample data
data = {
    "Department": ["IT", "IT", "HR", "HR", "Finance", "Finance"],
    "Employee": ["Aju", "Ben", "Anu", "Kiran", "Sam", "Riya"],
    "Salary": [50000, 52000, 45000, 46000, 60000, 62000]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Group by department and calculate average salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:\n", avg_salary)

# Multiple aggregations
stats = df.groupby("Department")["Salary"].agg(["min", "max", "mean"])
print("\nSalary Stats by Department:\n", stats)
