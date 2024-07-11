from database import get_connections
class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.category = None

    # Implement additional product-related methods here

    def __str__(self):
        return f"{self.product_name} - Price: ${self.price} - Quantity: {self.quantity}"

    def get_all_products():
        connection = get_connections()
        cursor = connection.cursor()
        query = """ SELECT product_id, product_name, price, quantity FROM inventory;"""
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def need_to_order():
        connection = get_connections()
        cursor = connection.cursor()
        query = """ SELECT product_id, product_name 
        FROM inventory
        WHERE quantity <= 5;"""
        cursor.execute(query)
        result = cursor.fetchall()
        return result

print(Product.need_to_order())

productlist = {item[0]: {'product_name': item[1], 'price': item[2], 'quantity': item[3]} for item in Product.get_all_products()}
print(productlist)

