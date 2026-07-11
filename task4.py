import os

FILE_NAME = "users.txt"

# Register Function
def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Create file if it doesn't exist
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

    # Check if username already exists
    with open(FILE_NAME, "r") as file:
        users = file.readlines()
        for user in users:
            saved_username = user.strip().split(",")[0]
            if username == saved_username:
                print("Username already exists!")
                return

    # Save new user
    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration Successful!")


# Login Function
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if not os.path.exists(FILE_NAME):
        print("No users registered yet.")
        return

    with open(FILE_NAME, "r") as file:
        users = file.readlines()

    for user in users:
        saved_username, saved_password = user.strip().split(",")

        if username == saved_username and password == saved_password:
            print("Login Successful!")
            return

    print("Invalid Username or Password!")


# Main Menu
while True:
    print("\n====== Login System ======")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thanks for using!")
        break

    else:
        print("Invalid Choice!")
