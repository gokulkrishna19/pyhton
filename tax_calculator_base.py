# tax_calculator.py
def calculate_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return 0.05 * income
    elif income <= 1000000:
        return 0.2 * income
    else:
        return 0.3 * income

incomes = [300000, 600000, 1200000]
with open("tax_report.txt", "w") as f:
    for income in incomes:
        tax = calculate_tax(income)
        f.write(f"Income: {income}, Tax: {tax}\n")

print("Tax report saved to tax_report.txt")
