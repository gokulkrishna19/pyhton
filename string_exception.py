# string_exception.py
# Program to demonstrate exception handling in string operations

def get_char_at(string, index):
    try:
        return string[index]
    except IndexError:
        return "⚠️ Index out of range!"
    except TypeError:
        return "⚠️ Invalid type for index!"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {e}"

def main():
    print("=== String Character Fetch with Exception Handling ===")
    text = input("Enter a string: ")
    
    try:
        idx = int(input("Enter index number: "))
        result = get_char_at(text, idx)
        print("Result:", result)
    except ValueError:
        print("⚠️ Please enter a valid integer for index.")

if __name__ == "__main__":
    main()
