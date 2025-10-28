# Program: Find common characters between two strings
# Author: Gokul Krishna
# Description: Displays all common characters between two strings (case-sensitive, ignores spaces).
# Returns -1 if no matching characters are found.

def find_common_characters(msg1, msg2):
    result = ''
    for i in msg1:
        if i != ' ' and i in msg2 and i not in result:
            result += i
    if result:
        return result
    else:
        return -1

# Provide different values for msg1 and msg2 to test the program
msg1 = "I like Python"
msg2 = "Java is a very popular language"

common_characters = find_common_characters(msg1, msg2)
print(common_characters)
