# diamond_numbers.py
# Prints a diamond-shaped number pattern

def print_diamond_numbers(n):
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()


if __name__ == "__main__":
    n = int(input("Enter the size of diamond: "))
    print("\nDiamond Number Pattern:\n")
    print_diamond_numbers(n)