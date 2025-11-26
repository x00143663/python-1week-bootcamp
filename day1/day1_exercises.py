# day1_exercises.py
# Day1 1 - Ex 1: variables and data types

name = "Nicolae"
age = 30          
town = "Naas"
is_student = False

print(f"My name is {name}, I'm {age} yers old, I live in {town} and is_student={is_student}.")

# -----------------------------
# Day 1 - Ex 2: input și output
# -----------------------------

name_user = input("Imput your name: ")
age_user = input("Imput your age: ")
town_user = input("Imput your town where toy live: ")

print(f"Hi, {name_user}! You have {age_user} years and you are living in {town_user}.")

# -----------------------------
# Ziua 1 - Exercițiul 3: condiții if / elif / else
# -----------------------------

age_input = input("Input your age: ")
age = int(age_input)

if age < 18:
    print("You are minor.")
elif age <= 65:
    print("You are adult.")
else:
    print("You are senior.")
#
# -----------------------------
# Day 1 - Ex 4: Loop for, odd and even numbers
# -----------------------------

print("I will display numbers from 1 to 20 and I tell if are odd or even:")

for number in range(1, 21):
    if number % 2 == 0:
        print(f"{number} - EVEN")
    else:
        print(f"{number} - ODD")

