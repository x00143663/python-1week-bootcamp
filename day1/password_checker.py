# password_checker.py
# Mini-project Day 1: Password checker

def is_strong_password(password: str) -> bool:
    """this function check if the password comply to the given rules."""
    has_min_length = len(password) >= 8
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    
    is_strong = has_min_length and has_upper and has_lower and has_digit

    print("Paswword check:")
    print(f"- Minimal length 8 character: {'OK' if has_min_length else 'NO'}")
    print(f"- Contain capital letter: {'OK' if has_upper else 'NO'}")
    print(f"- Contain lowercase letters: {'OK' if has_lower else 'NO'}")
    print(f"- Contain numbers: {'OK' if has_digit else 'NO'}")

    return is_strong


if __name__ == "__main__":
    pwd = input("Imput the password: ")

    if is_strong_password(pwd):
        print("\n The password is secure")
    else:
        print("\n The password is NOT secure!")

