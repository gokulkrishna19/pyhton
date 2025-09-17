# prime_check.py
# Program to check if a number is prime

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    print("=== Prime Number Checker ===")
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(f"✅ {num} is a prime number")
        else:
            print(f"❌ {num} is not a prime number")
    except ValueError:
        print("⚠️ Please enter a valid integer!")

if __name__ == "__main__":
    main()