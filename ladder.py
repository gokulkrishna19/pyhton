# ladder_patterns.py
# Prints different "ladder" patterns (simple, dashed, hollow)
# Author: Gokul (example)
# Usage: run and follow prompts, or import functions from this file.

def ladder_simple(height, rung_len=4):
    """Simple ladder: two rails '|' with solid rungs made of '='."""
    for i in range(height):
        print("|" + " " * rung_len + "|")
        # print rung
        print("|" + "=" * rung_len + "|")

def ladder_dashed(height, rung_len=6, gap=2):
    """Dashed ladder: alternating dashed rungs and gaps to look like steps."""
    for i in range(height):
        # rail line
        print("|" + " " * rung_len + "|")
        # dashed rung
        dash = "- " * (rung_len // 2)
        # trim/pad to exact rung_len
        dash = dash[:rung_len].ljust(rung_len)
        print("|" + dash + "|")
    # final rail top
    print("|" + " " * rung_len + "|")

def ladder_hollow(height, rung_len=8):
    """Hollow ladder: rungs are just edge characters, leaving inner space."""
    rail = "|"
    for i in range(height):
        print(rail + " " * rung_len + rail)
        # hollow rung: rails plus border chars, spaces inside
        if rung_len >= 2:
            print(rail + "[" + " " * (rung_len - 2) + "]" + rail)
        else:
            # small rung fallback
            print(rail + "-" * rung_len + rail)

def print_menu():
    print("\nLadder Pattern Generator")
    print("1. Simple Ladder (solid rungs)")
    print("2. Dashed Ladder (dashed rungs)")
    print("3. Hollow Ladder (rungs with hollow center)")
    print("4. All 3 patterns")
    print("0. Exit")

if __name__ == "__main__":
    while True:
        print_menu()
        try:
            choice = int(input("Choose pattern (0-4): ").strip())
        except ValueError:
            print("Please enter a number 0-4.")
            continue

        if choice == 0:
            print("Goodbye!")
            break

        try:
            h = int(input("Enter ladder height (number of steps, e.g. 4): ").strip())
            rl = int(input("Enter rung length (characters, e.g. 8): ").strip())
        except ValueError:
            print("Height and rung length must be integers. Try again.")
            continue

        print("\nResult:\n")
        if choice == 1:
            ladder_simple(h, rl)
        elif choice == 2:
            ladder_dashed(h, rl)
        elif choice == 3:
            ladder_hollow(h, rl)
        elif choice == 4:
            print("# Simple Ladder\n")
            ladder_simple(h, rl)
            print("\n# Dashed Ladder\n")
            ladder_dashed(h, rl)
            print("\n# Hollow Ladder\n")
            ladder_hollow(h, rl)
        else:
            print("Invalid choice. Pick 0-4.")

        input("\nPress Enter to continue...")