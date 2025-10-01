# do_while_guess.py
# Simulate do-while: keep asking until user guesses correctly

secret = 7

while True:  # do-while simulation
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("🎉 Correct! You guessed it!")
        break
    else:
        print("❌ Wrong, try again!")
