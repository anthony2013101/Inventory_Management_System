class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def list_products(self):
        return self.products
def get_all_categories(connection):
    category_list = []
    cursor = connection.cursor()
    query = """ SELECT * FROM categories"""
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    for c in cursor.fetchall():
        category_list.append(Category(**dict(zip(columns, c))))
    return category_list