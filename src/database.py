import mysql.connector
print("MySQL Connector installed successfully.")

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='root123!',
#     port='3306',
#     database='inventory_management'
# )

def get_connections():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Zoe94mak',
        port='3306',
        database='inventory_management'
    )
    return connection

# Create database
def print_database():
    connection = get_connections()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM inventory""")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

print(print_database())
