# number_pyramid.py

def number_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces
        print(" " * (n - i), end="")
        # Print numbers increasing
        for j in range(1, i + 1):
            print(j, end="")
        # Print numbers decreasing
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

if __name__ == "__main__":
    n = int(input("Enter the height of pyramid: "))
    print("\nNumber Pyramid Pattern:\n")
    number_pyramid(n)
