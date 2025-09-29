# fibonacci.py
# Program to generate Fibonacci sequence up to n terms

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("=== Fibonacci Sequence Generator ===")
    try:
        n = int(input("Enter number of terms: "))
        if n <= 0:
            print("⚠️ Please enter a positive integer.")
        else:
            print(f"Fibonacci sequence ({n} terms):", fibonacci(n))
    except ValueError:
        print("⚠️ Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
