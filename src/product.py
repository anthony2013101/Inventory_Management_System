class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = None

    # Implement additional product-related methods here
    def all_products():
        connection = get_connections()
        cursor = connection.cursor()
        cursor.execute("""SELECT product_id, product_name, price, quantity FROM inventory;""")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    print(all_products())