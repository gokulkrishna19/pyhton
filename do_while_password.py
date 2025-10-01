# do_while_password.py
# Simulate do-while loop: keep asking until correct password entered

correct_password = "python123"

while True:  # do-while simulation
    entered = input("Enter password: ")
    if entered == correct_password:
        print("✅ Access granted!")
        break
    else:
        print("❌ Wrong password, try again.")
