# guess_number.py
# Fun number guessing game

import random

def main():
    print("=== Number Guessing Game ===")
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            attempts += 1
            if guess < secret:
                print("Too low! 📉")
            elif guess > secret:
                print("Too high! 📈")
            else:
                print(f"🎉 Correct! The number was {secret}. Attempts: {attempts}")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!")

if __name__ == "__main__":
    main()
