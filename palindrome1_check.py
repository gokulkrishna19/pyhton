# Python program to check if a string is palindrome

def is_palindrome(text):
    # Remove spaces and convert to lowercase for uniform comparison
    text = text.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return text == text[::-1]

# Example input
word = input("Enter a word: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome ✅")
else:
    print(f"'{word}' is not a palindrome ❌")
