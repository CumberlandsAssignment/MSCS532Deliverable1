from inventory import InventoryManager, Product


def main():

    inventory = InventoryManager()

    # Create products
    p1 = Product("SKU1", "Laptop", "electronics", 1200, 5)
    p2 = Product("SKU2", "Mouse", "electronics", 25, 50)
    p3 = Product("SKU3", "Keyboard", "electronics", 70, 10)
    p4 = Product("SKU4", "Monitor", "electronics", 300, 3)

    # Add products to system
    inventory.add_product(p1)
    inventory.add_product(p2)
    inventory.add_product(p3)
    inventory.add_product(p4)

    # Lookup product
    product = inventory.get_product("SKU1")
    print("Lookup Product:")
    print(product.name, product.price, product.quantity)

    # Reorder alerts
    print("\nProducts needing reorder:")
    alerts = inventory.reorder_alerts(2)

    for quantity, sku in alerts:
        p = inventory.get_product(sku)
        print(p.name, "- Quantity:", quantity)

    # Price range query
    print("\nProducts priced between $20 and $100:")

    products = inventory.list_by_price("electronics", 20, 100)

    for p in products:
        print(p.name, "-", p.price)


if __name__ == "__main__":
    main()