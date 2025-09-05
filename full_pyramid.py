# star_pyramids.py

def half_pyramid(n):
    for i in range(1, n + 1):
        print("* " * i)

def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        print("* " * i)

def full_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

def inverted_full_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)

def diamond_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)

if __name__ == "__main__":
    n = 5  # Height of the pyramid
    
    print("1. Half Pyramid")
    half_pyramid(n)
    print("\n2. Inverted Half Pyramid")
    inverted_half_pyramid(n)
    print("\n3. Full Pyramid")
    full_pyramid(n)
    print("\n4. Inverted Full Pyramid")
    inverted_full_pyramid(n)
    print("\n5. Diamond Pyramid")
    diamond_pyramid(n)