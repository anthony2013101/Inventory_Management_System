from product import Product
from category import Category

class InventoryManagement:
    def __init__(self):
        self.categories = []
        self.products = []

    def create_category(self, category_id, name):
        for category in self.categories:
            if category.category_id == category_id or category.name == name:
                return f"Category with ID {category_id} or name '{name}' already exists."
        category = Category(category_id, name)
        self.categories.append(category)
        return category

    def find_category(self, category_id):
        for category in self.categories:
            if category.category_id == category_id:
                return category
        return f"Category was not found in the inventory"

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
        return product

    def remove_product(self, product):
        if product not in self.products:
            raise ValueError("There is no {product.name} found in the Inventory.")
        self.products.remove(product)
        product.category.remove_product(product)
        return f'{product.name} has been removed from Inventory.'

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
                return f'{product.name} has been updated'
        return f'Product with ID {product_id} was not found.'

    def update_category(self, category_id, new_name):
        for category in self.categories:
            if category.category_id == category_id:
                category.name = new_name
                return f'Category with ID {category_id} has been updated to {new_name}'


inventory_manager = InventoryManagement()
anthony = inventory_manager.create_category(1234, 'Anthony')
print(anthony.name)