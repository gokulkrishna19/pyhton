# do_while_menu.py
# Simple calculator using do-while style loop

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "⚠️ Division by zero!"

while True:  # do-while simulation
    print("\n=== Calculator Menu ===")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "5":
        print("👋 Exiting calculator...")
        break

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        
        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", sub(x, y))
        elif choice == "3":
            print("Result:", mul(x, y))
        elif choice == "4":
            print("Result:", div(x, y))
        else:
            print("⚠️ Invalid choice!")

    except ValueError:
        print("⚠️ Please enter valid numbers.")
