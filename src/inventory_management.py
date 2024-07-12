from src.product import Product, get_all_products
from src.category import Category, get_all_categories
from src.database import get_connections

class InventoryManagement:
    def __init__(self):
        self.connection = get_connections()
        self.categories = get_all_categories(self.connection)
        self.products = get_all_products(self.connection)

    def create_category(self, category_id, name):
        for category in self.categories:
            if category.category_id == category_id or category.name == name:
                return f"Category with ID {category_id} or name '{name}' already exists."
        category = Category(category_id, name)
        self.categories.append(category)
        self.save_category(category)
        return f"Category with ID {category_id} and name {name} has been created."

    def save_category(self, category):
        cursor = self.connection.cursor()
        query = "INSERT INTO categories (category_id, name) VALUES (%s, %s)"
        cursor.execute(query, (category.category_id, category.name))
        self.connection.commit()

    def find_category(self, category_id):
        for category in self.categories:
            if category.category_id == category_id:
                return category
        return None
    def create_product(self, product_id, name, price, quantity, category_id):
        category = self.find_category(category_id)
        if not category:
            return f"Cannot find category. The category will need to be created first."
        for product in self.products:
            if product.product_id == product_id:
                return f"Product with ID {product_id} already exists."
        product = Product(product_id, name, price, quantity)
        product.category = category
        category.add_product(product)
        self.products.append(product)
        self.save_product(product)
        return print(f"Added {quantity} {name}s at ${price} each the inventory")

    def save_product(self, product):
        cursor = self.connection.cursor()
        query = "INSERT INTO products (product_id, name, price, quantity, category_id) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (product.product_id, product.name, product.price, product.quantity, product.category_id))
        self.connection.commit()

    def remove_product(self, product_id):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product is None:
            raise ValueError(f"There is no product with ID {product_id} found in the Inventory.")
        self.products.remove(product)
        category = self.find_category(product.category_id)  # Retrieve the category object
        if category is not None:
            category.remove_product(product)
        self.delete_product(product)
        return f'{product.name} has been removed from Inventory.'


    def delete_product(self, product):
        cursor = self.connection.cursor()
        query = "DELETE FROM products WHERE product_id = %s"
        cursor.execute(query, (product.product_id,))
        self.connection.commit()


    def list_categories(self):
        return self.categories

    def list_products(self):
        return self.products

    def update_product(self, product_id, new_name, new_price, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.name = new_name
                product.price = new_price
                product.quantity = new_quantity
                self.save_product_update(product)
                return f'{product.name} has been updated'
        return f'Product with ID {product_id} was not found.'

    def save_product_update(self, product):
        cursor = self.connection.cursor()
        query = "UPDATE products SET name = %s, price = %s, quantity = %s WHERE product_id = %s"
        cursor.execute(query, (product.name, product.price, product.quantity, product.product_id))
        self.connection.commit()

    def update_category(self, category_id, new_name):
        for category in self.categories:
            if category.category_id == category_id:
                category.name = new_name
                self.save_category_update(category)
                return f'Category with ID {category_id} has been updated to {new_name}'
        return f"Category with ID {category_id} was not found."

    def save_category_update(self, category):
        cursor = self.connection.cursor()
        query = "UPDATE categories SET name = %s WHERE category_id = %s"
        cursor.execute(query, (category.name, category.category_id))
        self.connection.commit()

    def display_inventory(self):
        """
        Displays the current inventory of products.
        """
        print("Current Inventory:")
        print("------------------")

        if not self.products:
            print("No products in the inventory.")
            return

        for product in self.products:
            print(
                f"{product.name} - Price: ${product.price} - Quantity: {product.quantity} - Category: {product.category_id}")

        print("------------------")
        print(f"Total Products: {len(self.products)}")