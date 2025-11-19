import pandas as pd

# Creating a sample DataFrame
data = {
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [60000, 800, 1500],
    "Stock": [10, 50, 20]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

# Saving to CSV
df.to_csv("products.csv", index=False)
print("\nFile 'products.csv' created successfully!")

# Reading the saved CSV
df_read = pd.read_csv("products.csv")
print("\nReading CSV:\n", df_read)
