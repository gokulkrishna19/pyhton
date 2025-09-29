# string_to_int_exception.py
# Program to demonstrate exception handling while converting string to integer

def convert_to_int(s):
    try:
        return int(s)
    except ValueError:
        return "⚠️ Cannot convert to integer. Please enter digits only."
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"

def main():
    print("=== String to Integer Conversion with Exception Handling ===")
    user_input = input("Enter a number as string: ")
    result = convert_to_int(user_input)
    print("Result:", result)

if __name__ == "__main__":
    main()
