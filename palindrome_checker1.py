# palindrome_checker.py
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

words = ["Madam", "Racecar", "Infosys", "Malayalam"]

for w in words:
    if is_palindrome(w):
        print(f"'{w}' is a palindrome ✅")
    else:
        print(f"'{w}' is not a palindrome ❌")
