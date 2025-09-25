# Python program with array of names (using list)

# Create an array of names
names = ["Alice", "Bob", "Charlie", "David"]

print("Original Names Array:", names)

# Access elements
print("First name:", names[0])
print("Last name:", names[-1])

# Insert a new name
names.append("Eve")
print("After appending 'Eve':", names)

# Insert at specific position
names.insert(2, "Frank")
print("After inserting 'Frank' at index 2:", names)

# Remove a name
names.remove("Charlie")
print("After removing 'Charlie':", names)

# Update a name
names[1] = "Robert"
print("After updating index 1 with 'Robert':", names)

# Traverse array
print("Traversing names:")
for name in names:
    print(name)

# Length of array
print("Total number of names:", len(names))