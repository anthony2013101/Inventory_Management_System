class Product:
    def __init__(self, product_id, name, price, quantity, category_id = None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category_id = category_id

    def __str__(self):
        return f"{self.name} - Price: ${self.price} - Quantity: {self.quantity}"

def get_all_products(connection):
    product_list = []
    cursor = connection.cursor()
    query = """ SELECT * FROM products"""
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    for product in cursor.fetchall():
        product_list.append(Product(**dict(zip(columns, product))))
    return product_list