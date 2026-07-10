def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\n----- Caesar Cipher -----")
print("Original Message :", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
