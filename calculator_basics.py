def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Cannot divide by zero"

print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1: print("Result:", add(a, b))
elif choice == 2: print("Result:", sub(a, b))
elif choice == 3: print("Result:", mul(a, b))
elif choice == 4: print("Result:", div(a, b))
else: print("Invalid choice")
