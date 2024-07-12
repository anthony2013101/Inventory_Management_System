from src.inventory_management import InventoryManagement
from src.database import get_connections
from src.product import get_all_products
from time import sleep

def main():
    inventory = InventoryManagement()

    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Create New Category")
        print("4. Update Product Info")
        print("5. Update Category Name")
        print("6. Display Inventory")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input('Enter Product ID: '))
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            category_id = int(input('Enter Category ID: '))
            result = inventory.create_product(product_id, name, price, quantity, category_id)
            print(result)

        elif choice == '2':
            product_id = int(input('Enter Product ID: '))
            result = inventory.remove_product(product_id)
            print(result)

        elif choice == '3':
            category_id = int(input("Enter Category ID: "))
            name = str(input("Enter name: "))
            result = inventory.create_category(category_id, name)
            print(result)
            sleep(5)

        elif choice == '4':
            product_id = int(input('Enter Product ID: '))
            new_name = input("Enter new item name: ")
            new_quantity = int(input("Enter new quantity: "))
            new_price = float(input("Enter new price: "))
            result = inventory.update_product(product_id, new_name, new_price, new_quantity)
            print(result)

        elif choice == '5':
            category_id = int(input("Enter Category ID: "))
            new_name = str(input("Enter name: "))
            result = inventory.update_category(category_id, new_name)
            print(result)

        elif choice == '6':
            result = inventory.display_inventory()
            print(result)

        elif choice == '7':
            print("Exiting the Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


