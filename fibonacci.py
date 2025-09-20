# fibonacci.py
# Program to generate Fibonacci series up to n terms

def fibonacci(n: int):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("=== Fibonacci Series ===")
    try:
        n = int(input("Enter number of terms: "))
        if n <= 0:
            print("⚠️ Please enter a positive integer!")
        else:
            print(f"Fibonacci series ({n} terms): {fibonacci(n)}")
    except ValueError:
        print("⚠️ Invalid input, enter a number!")

if __name__ == "__main__":
    main()
