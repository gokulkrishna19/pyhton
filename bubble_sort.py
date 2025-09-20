# bubble_sort.py
# Program to sort an array using Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
    return arr

def main():
    print("=== Bubble Sort ===")
    try:
        arr = list(map(int, input("Enter numbers separated by space: ").split()))
        if not arr:
            print("⚠️ Array cannot be empty!")
            return
        print("Original array:", arr)
        sorted_arr = bubble_sort(arr)
        print("Sorted array:", sorted_arr)
    except ValueError:
        print("⚠️ Please enter valid integers!")

if __name__ == "__main__":
    main()
