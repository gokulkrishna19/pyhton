# ============================
# Tuple Example Program in Python
# ============================

# 1. Creating tuples
player = ("Messi", "Argentina", 819)
student = ("Gokul", 21, "Kerala")
numbers = (1, 2, 3, 4, 5, 3, 2, 1)

print("Player Tuple:", player)
print("Student Tuple:", student)
print("Numbers Tuple:", numbers)
print()

# 2. Accessing elements
print("First player element:", player[0])      # Messi
print("Last student element:", student[-1])   # Kerala
print("Slice from numbers:", numbers[1:4])    # (2, 3, 4)
print()

# 3. Unpacking tuples
name, age, place = student
print("Unpacked Student Data -> Name:", name, ", Age:", age, ", Place:", place)
print()

# 4. Looping through tuple
print("Looping through player tuple:")
for item in player:
    print(" ->", item)
print()

# 5. Nested tuple
match = ("Kerala Blasters", ("Bengaluru FC", 2, 1))
print("Nested Tuple Example:", match)
print("Opponent Team:", match[1][0])   # Bengaluru FC
print("Score:", match[1][1], "-", match[1][2])
print()

# 6. Tuple methods
print("Count of '2' in numbers tuple:", numbers.count(2))   # 2
print("Index of '3' in numbers tuple:", numbers.index(3))   # 2 (first occurrence)
print()

# 7. Tuple immutability demo
try:
    player[0] = "Ronaldo"   # ❌ not allowed
except TypeError as e:
    print("Error: Tuples are immutable ->", e)
print()

# 8. Real-world example: Storing multiple match records
matches = [
    ("Kerala Blasters", "Bengaluru FC", 3, 1),
    ("ATK Mohun Bagan", "Mumbai City", 2, 2),
    ("Chennaiyin FC", "Hyderabad FC", 1, 0)
]

print("Match Records:")
for t1, t2, s1, s2 in matches:
    print(f" {t1} {s1} - {s2} {t2}")
