from src.inventory_management import InventoryManagement

def main():
    inventory = InventoryManagement()
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
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.add_item(item_name, quantity, price)

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
    