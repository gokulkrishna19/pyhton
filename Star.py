# star_pyramids_dict.py

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

# Dictionary mapping choices to functions
patterns = {
    1: ("Half Pyramid", half_pyramid),
    2: ("Inverted Half Pyramid", inverted_half_pyramid),
    3: ("Full Pyramid", full_pyramid),
    4: ("Inverted Full Pyramid", inverted_full_pyramid),
    5: ("Diamond Pyramid", diamond_pyramid),
}

if __name__ == "__main__":
    n = int(input("Enter the height of pyramid: "))

    print("\nAvailable Patterns:")
    for key, (name, _) in patterns.items():
        print(f"{key}. {name}")

    choice = int(input("Enter your choice (1-5): "))

    if choice in patterns:
        print(f"\n{patterns[choice][0]}:\n")
        patterns[choice][1](n)  # Call the selected function
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")