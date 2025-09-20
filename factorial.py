# factorial.py
# Program to calculate factorial of a number (iterative & recursive)

def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("=== Factorial Calculator ===")
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("⚠️ Factorial is not defined for negative numbers!")
            return

        print(f"Iterative Factorial of {num}: {factorial_iterative(num)}")
        print(f"Recursive Factorial of {num}: {factorial_recursive(num)}")
    except ValueError:
        print("⚠️ Please enter a valid integer!")

if __name__ == "__main__":
    main()
