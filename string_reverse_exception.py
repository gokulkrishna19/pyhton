# string_reverse_exception.py
# Program to reverse a string with exception handling

def reverse_string(s):
    try:
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        if len(s) == 0:
            raise ValueError("String cannot be empty")
        return s[::-1]
    except TypeError as te:
        return f"⚠️ Error: {te}"
    except ValueError as ve:
        return f"⚠️ Error: {ve}"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"

def main():
    print("=== String Reverse with Exception Handling ===")
    text = input("Enter a string: ")
    result = reverse_string(text)
    print("Result:", result)

if __name__ == "__main__":
    main()
