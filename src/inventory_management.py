from product import Product
from category import Category

class InventoryManagement:
    def __init__(self):
        self.categories = []
        self.products = {}

    def add_item(self, product_id, name, price, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
        else:
            self.products[product_id] = Product(product_id, name, price, quantity)
        print(f"Added {quantity} of {name} at ${price} each to the inventory.")

    def remove_item(self, product_id, name, quantity):
        if product_id in self.products:
            if self.products[product_id].quantity >= quantity:
                self.products[product_id].quantity -= quantity
                if self.products[product_id].quantity== 0:
                    del self.products[product_id]
                print(f"Removed {quantity} of {name} from the inventory.")
            else:
                print(f"Error: Not enough quantity of {name} to remove.")
        else:
            print(f"Error: {name} not found in inventory.")

    def update_price(self, product_id, name, new_price):
        if product_id in self.products:
            self.products[product_id].price = new_price
            print(f"Updated price of {name} to ${new_price}.")
        else:
            print(f"Error: {name} not found in inventory.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product_id, product in self.products.items():
                print(f"Item: {product.name}, Quantity: {product.quantity}, Price: ${product.price}")


# Create an instance of Inventory
inventory = InventoryManagement()

# Adjust items to the inventory
inventory.add_item(1, "shoes", 59, 100)
inventory.add_item(2, "shirts", 29, 50)
inventory.remove_item(1, "shoes", 5)
inventory.update_price(1,"shoes",69)
inventory.display_inventory()

# Print the inventory
print(inventory)