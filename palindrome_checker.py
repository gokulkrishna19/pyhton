def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

word = input("Enter a word: ")
print("Palindrome ✅" if is_palindrome(word) else "Not a palindrome ❌")
