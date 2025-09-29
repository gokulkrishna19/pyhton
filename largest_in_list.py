# largest_in_list.py
# Program to find the largest element in a list

def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def main():
    print("=== Largest Element Finder ===")
    try:
        # Input: space-separated integers
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        
        largest = find_largest(nums)
        if largest is not None:
            print("The largest number is:", largest)
        else:
            print("⚠️ The list is empty!")
    except ValueError:
        print("⚠️ Please enter only integers!")

if __name__ == "__main__":
    main()
