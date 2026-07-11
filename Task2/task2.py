import re

password = input("Enter your password: ")

score = 0

print("\n----- Password Analysis -----")

# Check Length
if len(password) >= 8:
    print("✔ Minimum Length (8+)")
    score += 1
else:
    print("✘ Minimum Length (8+)")

# Check Uppercase
if re.search(r"[A-Z]", password):
    print("✔ Uppercase Letter")
    score += 1
else:
    print("✘ Uppercase Letter")

# Check Lowercase
if re.search(r"[a-z]", password):
    print("✔ Lowercase Letter")
    score += 1
else:
    print("✘ Lowercase Letter")

# Check Number
if re.search(r"[0-9]", password):
    print("✔ Number")
    score += 1
else:
    print("✘ Number")

# Check Special Character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("✔ Special Character")
    score += 1
else:
    print("✘ Special Character")

print("\nScore:", score)

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
