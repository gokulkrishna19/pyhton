text = input("Enter a word/number: ")

if text == text[::-1]:
    print("✅ It's a palindrome")
else:
    print("❌ Not a palindrome")