# Python program to check palindrome using list

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    
    # Convert string to list
    char_list = list(text)
    
    # Create a reversed copy of the list
    reversed_list = char_list[::-1]
    
    # Compare both lists
    return char_list == reversed_list

# Example input
word = input("Enter a word: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome ✅")
else:
    print(f"'{word}' is not a palindrome ❌")
