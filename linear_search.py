# linear_search.py
# Program to perform Linear Search in an array

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return index
    return -1

def main():
    print("=== Linear Search in Array ===")
    try:
        arr = list(map(int, input("Enter numbers separated by space: ").split()))
        target = int(input("Enter the number to search: "))

        index = linear_search(arr, target)
        if index != -1:
            print(f"✅ {target} found at position {index + 1} (index {index})")
        else:
            print(f"❌ {target} not found in array")
    except ValueError:
        print("⚠️ Please enter valid integers!")

if __name__ == "__main__":
    main()

