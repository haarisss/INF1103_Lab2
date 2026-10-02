

inventory =  [{"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
              {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
              {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


def display_all():
    print("Current Inventory")
    print("------------------------------------------------")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("------------------------------------------------")
    
    
def add_product():
    print("Add New Product")
    inventory_id = input("Product ID: ")
    inventory_name = input("Product Name: ")
    inventory_price = float(input("Price: "))
    inventory_stock = int(input("Stock Quantity: "))
    new_product = {
        "id": inventory_id,
        "name": inventory_name,
        "price": inventory_price,
        "stock": inventory_stock
    }
    inventory.append(new_product)
    print("Product added successfully!")
    

def update_stock():
    print("Update Stock")
    search_id = input("Enter Product ID: ")
    found = False
    for product in inventory:
        if product["id"] == search_id:
            found = True
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock
            print("Stock updated successfully!")
    if not found:
        print("Product not found.")


def search_product():
    print("Search Product")
    search_id = input("Enter Product ID: ")
    found = False
    for product in inventory:
        if product["id"] == search_id:
            found = True
            print("Product Found")
            print("--------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("--------------------")
    if not found:
        print("Product not found.")
    

search_product()
add_product()
display_all()
update_stock()
display_all()
