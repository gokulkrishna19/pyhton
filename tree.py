# tree_pattern.py
# Prints a star tree pattern with trunk

def print_tree(n):
    # Tree part (pyramid levels)
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

    # Trunk (2 lines, centered)
    for _ in range(2):
        print(" " * (n - 1) + "||")


if __name__ == "__main__":
    height = int(input("Enter tree height: "))
    print("\nTree Pattern:\n")
    print_tree(height)