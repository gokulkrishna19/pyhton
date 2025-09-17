# count_vowels.py
# Program to count vowels in a string

def count_vowels(text: str) -> int:
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

def main():
    print("=== Vowel Counter ===")
    sentence = input("Enter a string: ")
    count = count_vowels(sentence)
    print(f"Total vowels in '{sentence}': {count}")

if __name__ == "__main__":
    main()