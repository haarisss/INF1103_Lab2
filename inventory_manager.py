import json
import os

inventory = []


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
        
        
def load_inventory():
    global inventory
    if os.path.exists("inventory.json"):
        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()
        print("inventory.json found.")
        print("Inventory loaded successfully.")
    else:
        inventory = []
        print("No inventory.json found. Starting with empty inventory.")
        

def save_inventory():
    file = open("inventory.json", "w")
    json.dump(inventory, file, indent=4)
    file.close()
    print("Inventory saved successfully to inventory.json.")

def menu():
    while True:
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")
        choice = input("Enter option: ")

        if choice == "1":
            display_all()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            search_product()
        elif choice == "5":
            save_inventory()
        elif choice == "6":
            save_inventory()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option, try again.")
    
load_inventory()
menu()
