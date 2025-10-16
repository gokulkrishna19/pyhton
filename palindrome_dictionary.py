# Python program to check palindrome using dictionary

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    n = len(text)
    
    # Store each character in a dictionary with its index
    char_dict = {i: text[i] for i in range(n)}
    
    # Compare characters from start and end
    for i in range(n // 2):
        if char_dict[i] != char_dict[n - i - 1]:
            return False
    return True

# Example input
word = input("Enter a word: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome ✅")
else:
    print(f"'{word}' is not a palindrome ❌")
