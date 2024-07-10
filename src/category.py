class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name
        self.products = []

    # Implement additional category-related methods here

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def list_products(self):
        return self.products


