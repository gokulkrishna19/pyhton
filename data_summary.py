import pandas as pd

def summarize_csv(file_path):
    data = pd.read_csv(file_path)
    print("Shape:", data.shape)
    print("\nColumns:", data.columns)
    print("\nMissing values:\n", data.isnull().sum())
    print("\nBasic Stats:\n", data.describe())

# Example use
# summarize_csv("data.csv")
