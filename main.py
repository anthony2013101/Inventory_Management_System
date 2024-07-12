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

from src.inventory_management import InventoryManagement
def main():
    inventory = InventoryManagement()
    while login(users) == "Login successful!" == True:
        return True
    # Implement your inventory management system operations here

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item Price")
    print("4. Display Inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        product_id = input("Enter product ID: ")
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        category_id = input("Enter category ID: ")
        category_name = input("Enter category name: ")
        InventoryManagement.add_item(product_id, product_name, quantity, price, category_id, category_name)

    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to remove: "))
        inventory.remove_item(item_name, quantity)

    elif choice == '3':
        item_name = input("Enter item name: ")
        new_price = float(input("Enter new price: "))
        inventory.update_price(item_name, new_price)

    elif choice == '4':
        inventory.display_inventory()

    elif choice == '5':
        print("Exiting the Inventory Management System.")
        break

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    