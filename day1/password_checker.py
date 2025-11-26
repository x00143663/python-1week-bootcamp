# password_checker.py
# Mini-proiect Ziua 1: Verificator de parolă

def is_strong_password(password: str) -> bool:
    """Verifică dacă parola este puternică după criteriile definite."""
    has_min_length = len(password) >= 8
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    # Poți adăuga și alte condiții (ex: simboluri speciale)
    is_strong = has_min_length and has_upper and has_lower and has_digit

    print("Verificare parolă:")
    print(f"- Lungime minimă 8 caractere: {'OK' if has_min_length else 'NU'}")
    print(f"- Conține litere mari:        {'OK' if has_upper else 'NU'}")
    print(f"- Conține litere mici:        {'OK' if has_lower else 'NU'}")
    print(f"- Conține cifre:              {'OK' if has_digit else 'NU'}")

    return is_strong


if __name__ == "__main__":
    pwd = input("Introdu parola pe care vrei să o verifici: ")

    if is_strong_password(pwd):
        print("\n✅ Parola este sigură!")
    else:
        print("\n❌ Parola NU este sigură! Încearcă să respecți toate criteriile de mai sus.")

