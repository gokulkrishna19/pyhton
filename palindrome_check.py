# palindrome_check.py
# Program to check if a string is a palindrome

def is_palindrome(s: str) -> bool:
    # Normalize string: remove spaces & lowercase
    s = ''.join(s.split()).lower()
    return s == s[::-1]

def main():
    print("=== Palindrome Checker ===")
    text = input("Enter a string: ")

    if is_palindrome(text):
        print(f"✅ '{text}' is a palindrome")
    else:
        print(f"❌ '{text}' is not a palindrome")

if __name__ == "__main__":
    main()
