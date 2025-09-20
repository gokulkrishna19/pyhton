# array_min_max.py
# Program to find the smallest and largest element in an array

def find_min_max(arr):
    smallest = min(arr)
    largest = max(arr)
    return smallest, largest

def main():
    print("=== Array Min & Max Finder ===")
    try:
        # Input array as space-separated integers
        arr = list(map(int, input("Enter numbers separated by space: ").split()))
        if not arr:
            print("⚠️ Array cannot be empty!")
            return

        smallest, largest = find_min_max(arr)
        print(f"Smallest element: {smallest}")
        print(f"Largest element: {largest}")
    except ValueError:
        print("⚠️ Please enter valid integers!")

if __name__ == "__main__":
    main()
