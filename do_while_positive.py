# do_while_positive.py
# Keep asking user until they enter a positive number

while True:  # do-while simulation
    num = int(input("Enter a positive number: "))
    if num > 0:
        print("✅ You entered:", num)
        break
    else:
        print("⚠️ Please enter a positive number.")
