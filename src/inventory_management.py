from product import Product
from category import Category

class InventoryManagement:
    def __init__(self):
        self.categories = []
        self.products = []

    # Implement inventory management methods here
    def create_category(self, category_id, name):
        category = Category(category_id, name)
        self.categories.append(name)
        return category

    def create_product(self, product_id, name, price, quantity, category):
        product = Product(product_id, name, price, quantity)
        product.category = category
        category.add_product(product)
        self.products.append(product)
        return product

    def remove_product(self, product):
        if product not in self.products:
            raise ValueError("There is no {product} found in the Inventory.")
        self.products.remove(product)
        return f'{product} has been removed from Inventory.'


inventory_manager = InventoryManagement()
anthony = inventory_manager.create_category(1234, 'Anthony')
print(anthony.name)