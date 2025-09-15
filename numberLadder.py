# number_ladder.py
# Prints a number ladder pattern

def number_ladder(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter number of steps for ladder: "))
    print("\nNumber Ladder Pattern:\n")
    number_ladder(n)
