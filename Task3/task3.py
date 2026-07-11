import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    password = []
    characters = ""

    # Ensure at least one character from each selected category
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
        characters += string.ascii_uppercase

    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
        characters += string.ascii_lowercase

    if use_digits:
        password.append(random.choice(string.digits))
        characters += string.digits

    if use_symbols:
        password.append(random.choice(string.punctuation))
        characters += string.punctuation

    if characters == "":
        return None

    # Check minimum length
    if length < len(password):
        print("\nError: Password length is too short for the selected options.")
        return None

    # Fill remaining characters
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)


def password_strength(length):
    if length < 8:
        return "Weak"
    elif length < 12:
        return "Medium"
    else:
        return "Strong"


def save_passwords(passwords):
    with open("generated_passwords.txt", "w") as file:
        for i, pwd in enumerate(passwords, start=1):
            file.write(f"{i}. {pwd}\n")
    print("\nPasswords saved successfully in 'generated_passwords.txt'")


def main():
    print("=" * 50)
    print("        RANDOM PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        try:
            length = int(input("\nEnter password length: "))
            if length <= 0:
                print("Length must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    upper = input("Include Uppercase letters? (y/n): ").lower() == "y"
    lower = input("Include Lowercase letters? (y/n): ").lower() == "y"
    digits = input("Include Numbers? (y/n): ").lower() == "y"
    symbols = input("Include Special Characters? (y/n): ").lower() == "y"

    if not (upper or lower or digits or symbols):
        print("\nError: You must select at least one character type.")
        return

    while True:
        try:
            count = int(input("\nHow many passwords do you want to generate? "))
            if count <= 0:
                print("Enter a value greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    passwords = []

    print("\nGenerated Password(s)")
    print("-" * 50)

    for i in range(count):
        pwd = generate_password(length, upper, lower, digits, symbols)
        if pwd:
            passwords.append(pwd)
            print(f"{i+1}. {pwd}")

    print("\nPassword Strength:", password_strength(length))

    save = input("\nDo you want to save the passwords to a file? (y/n): ").lower()

    if save == "y":
        save_passwords(passwords)

    print("\nThank you for using the Password Generator!")


if __name__ == "__main__":
    main()
