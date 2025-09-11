def first_unique_char(s):
    char_count = {}

    # Count frequency of each character
    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1

    # Find the first non-repeating character
    for i, ch in enumerate(s):
        if char_count[ch] == 1:
            return i
    return -1


# Driver code
s = input("Enter a string: ")
result = first_unique_char(s)
print("Index of first non-repeating character:", result)