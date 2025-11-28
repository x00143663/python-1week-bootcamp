# -----------------------------
# Day 2 - Exercise 1: Lists
# -----------------------------

# Create a list of fruits
fruits = ["apple", "banana", "orange", "kiwi"]

print("Initial list:", fruits)

# Add an item
fruits.append("mango")
print("After append:", fruits)

# Remove an item
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Sort the list
fruits.sort()
print("Sorted list:", fruits)

# Filter items that start with 'a'
filtered = [fruit for fruit in fruits if fruit.startswith("a")]
print("Items starting with 'a':", filtered)


# -----------------------------
# Day 2 - Exercise 2: Dictionaries
# -----------------------------

# Create a dictionary representing a user
user = {
    "name": "Nick",
    "age": 30,
    "city": "Naas"
}

print("\nUser dictionary:", user)

# Access values
print("Name:", user["name"])

# Add a new field
user["job"] = "Cloud Engineer"
print("After adding job:", user)

# Update fields
user["age"] = 31
print("After updating age:", user)

# Loop through keys and values
for key, value in user.items():
    print(f"{key} -> {value}")


# -----------------------------
# Day 2 - Exercise 3: Sets
# -----------------------------

# Create a set
unique_numbers = {1, 2, 3, 4, 4, 2, 1}
print("\nSet with duplicates removed:", unique_numbers)

# Add new value
unique_numbers.add(10)
print("After adding 10:", unique_numbers)

# Check membership
print("Is 3 in the set?", 3 in unique_numbers)

# Remove item
unique_numbers.discard(2)
print("After removing 2:", unique_numbers)

