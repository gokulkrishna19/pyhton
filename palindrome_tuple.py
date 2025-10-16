# Python program to check palindrome using tuple

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    
    # Convert string to tuple
    char_tuple = tuple(text)
    
    # Create a reversed tuple
    reversed_tuple = char_tuple[::-1]
    
    # Compare both tuples
    return char_tuple == reversed_tuple

# Example input
word = input("Enter a word: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome ✅")
else:
    print(f"'{word}' is not a palindrome ❌")
