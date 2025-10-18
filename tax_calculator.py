# Python program for a simple Tax Calculator

def calculate_tax(income):
    """
    Calculate income tax based on income slabs.
    (Example: Indian tax system for simplicity)
    """
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
    return tax

# Input from user
income = float(input("Enter your annual income (in ₹): "))

# Calculate tax
tax = calculate_tax(income)

# Display result
print(f"Your calculated tax is: ₹{tax:.2f}")

# Optionally display net income after tax
net_income = income - tax
print(f"Net income after tax: ₹{net_income:.2f}")
