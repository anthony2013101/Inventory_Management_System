from database import get_connections
class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
        self.products = []

    # Implement additional category-related methods here
    def __str__(self):
        return f"{self.category_name} - Price: ${self.price} - Quantity: {self.quantity}"

    def get_all_categories():
        connection = get_connections()
        cursor = connection.cursor()
        query = """ SELECT category_id, category_name, SUM(quantity) 
                    FROM inventory
                    GROUP BY category_id, category_name;"""
        cursor.execute(query)
        result = cursor.fetchall()
        return result

categorylist = [{'category_id':item[0], 'category_name': item[1], 'quantity': item[2]} for item in Category.get_all_categories()]
print(categorylist)
