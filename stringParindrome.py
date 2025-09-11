def is_palindrome(s):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# Driver code
s = input("Enter a string: ")
print("Palindrome?", is_palindrome(s))