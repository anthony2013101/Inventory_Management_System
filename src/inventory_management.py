from database import get_connections
from product import productlist
from category import categorylist

class InventoryManagement:

    def __init__(self):
        self.connection = get_connections()
        self.categories = categorylist
        self.products = productlist

    def add_item(self, product_id, product_name, quantity, price, category_id, category_name):
        if product_id in self.products:
            self.products[product_id]['quantity'] += quantity
            connection = get_connections()
            cursor = connection.cursor()
            query = """UPDATE inventory SET quantity = quantity + %s WHERE product_id = %s;"""
            cursor.execute(query, (quantity, product_id))
            connection.commit()
            result = cursor.fetchall()
            return result
        else:
            self.products[product_id] = {
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'category_id': category_id,
                'category_name': category_name
            }
            connection = get_connections()
            cursor = connection.cursor()
            query = """INSERT INTO inventory (product_id, product_name, quantity, price, category_id, category_name) VALUES (%s, %s, %s, %s, %s, %s);"""
            cursor.execute(query, (product_id, product_name, quantity, price, category_id, category_name))
            connection.commit()
            result = cursor.fetchall()
            return result
        print(f"Added {quantity} of {product_name} at ${price} each to the inventory.")

    def remove_item(self, product_id, product_name, quantity):
        if product_id in self.products:
            if self.products[product_id]['quantity'] >= quantity:
                self.products[product_id]['quantity']-= quantity
                connection = get_connections()
                cursor = connection.cursor()
                query = """UPDATE inventory SET quantity = quantity - %s WHERE product_id = %s;"""
                cursor.execute(query, (quantity, product_id))
                connection.commit()

                if self.products[product_id]['quantity'] == 0:
                    del self.products[product_id]
                    query = """DELETE FROM inventory WHERE product_id = %s;"""
                    cursor.execute(query, (product_id))
                    connection.commit()
                    result = cursor.fetchall()
                    return result
                print(f"Removed {quantity} of {product_name} from the inventory.")
            else:
                print(f"Error: Not enough quantity of {product_name} to remove.")
        else:
            print(f"Error: {product_name} not found in inventory.")

    def update_price(self, product_id, product_name, new_price):
        if product_id in self.products:
            self.products[product_id].price = new_price
            print(f"Updated price of {product_name} to ${new_price}.")
        else:
            print(f"Error: {product_name} not found in inventory.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product_id, product in self.products.items():
                print(f"Item: {product.product_name}, Quantity: {product.quantity}, Price: ${product.price}")


# Create an instance of Inventory
inventory = InventoryManagement()

# Adjust items to the inventory
inventory.add_item(30, "Kawhi Jersey", 0, 79.99, category_id=1, category_name="Jerseys")
inventory.remove_item(30, "Kawhi Jersey", 1)
#inventory.update_price(1,"shoes",69)
#inventory.display_inventory()

# Print the inventory
print(productlist)