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

