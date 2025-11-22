import pandas as pd

data = {
    "Product": ["Pen", "Book", "Pencil", "Bag"],
    "Price": [10, 120, 5, 450],
    "Stock": [100, 30, 200, 15]
}

df = pd.DataFrame(data)

# Filtering
print("Price > 20:\n", df[df["Price"] > 20])

# Sorting
print("\nSorted by Price:\n", df.sort_values(by="Price"))
