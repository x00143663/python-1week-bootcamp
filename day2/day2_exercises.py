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

