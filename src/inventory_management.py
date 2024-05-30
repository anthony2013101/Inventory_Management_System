from product import Product
from category import Category

class InventoryManagement:
    def __init__(self):
        self.categories = []
        self.products = []

    # Implement inventory management methods here

    def add_product(self, product):
        self.products.append(product)

    # Add more inventory management methods as needed