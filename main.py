from src.inventory_management import InventoryManagement
from src.database import get_connections
from src.product import get_all_products

def main():
    connection = get_connections()
    all_products = get_all_products(connection=connection)
    for product in all_products:
        print(product)
    inventory = InventoryManagement()
    print(inventory.create_category(1, 'Souvineer'))


if __name__ == "__main__":
    main()


