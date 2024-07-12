def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Sample users data
users = {
    "zoe": "password1",
    "anthony": "password2",
    "avi": "password3",
    "sifat": "password4"
}

login(users)

def maintest():
    if login(users) == "Login successful!":
        return True

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item Price")
    print("4. Display Inventory")
    print("5. Exit")