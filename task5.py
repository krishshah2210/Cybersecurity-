# XOR Encryption and Decryption

KEY = 123


def xor_file(input_file, output_file):
    with open(input_file, "rb") as file:
        data = file.read()

    encrypted_data = bytearray()

    for byte in data:
        encrypted_data.append(byte ^ KEY)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)


print("===== XOR File Encryption =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice: ")

if choice == "1":
    xor_file("message.txt", "encrypted.bin")
    print("Encryption Successful!")
    print("Encrypted file: encrypted.bin")

elif choice == "2":
    xor_file("encrypted.bin", "decrypted.txt")
    print("Decryption Successful!")
    print("Decrypted file: decrypted.txt")

else:
    print("Invalid Choice!")

