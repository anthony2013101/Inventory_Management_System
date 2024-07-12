import mysql.connector


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
        passwd='root123!',
        port='3306',
        database='inventory_management'
    )
    return connection
