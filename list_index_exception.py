# list_index_exception.py
# Program to demonstrate exception handling in list indexing

def get_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "⚠️ Error: Index out of range."
    except TypeError:
        return "⚠️ Error: Index must be an integer."
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"

def main():
    print("=== List Index Access with Exception Handling ===")
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        idx = int(input("Enter index to fetch: "))
        print("Result:", get_element(numbers, idx))
    except ValueError:
        print("⚠️ Please enter valid integers.")

if __name__ == "__main__":
    main()
