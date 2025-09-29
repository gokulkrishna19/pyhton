# safe_division.py
# Program to demonstrate exception handling in number division

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "⚠️ Error: Division by zero is not allowed."
    except TypeError:
        return "⚠️ Error: Both inputs must be numbers."
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"

def main():
    print("=== Safe Division Program ===")
    try:
        x = float(input("Enter numerator: "))
        y = float(input("Enter denominator: "))
        result = safe_divide(x, y)
        print("Result:", result)
    except ValueError:
        print("⚠️ Please enter valid numeric values.")

if __name__ == "__main__":
    main()
