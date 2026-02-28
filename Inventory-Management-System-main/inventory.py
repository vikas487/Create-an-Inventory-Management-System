import json

DATA_FILE = "inventory.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"products": [], "next_id": 1}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_product(data):
    print("\n--- Add New Product ---")
    name = input("Product Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    category = input("Category: ").strip()
    price = input("Price: ").strip()
    qty = input("Quantity: ").strip()

    try:
        price = float(price)
        qty = int(qty)
    except ValueError:
        print("Error: Invalid price or quantity.")
        return

    product = {
        "id": data["next_id"],
        "name": name,
        "category": category,
        "price": price,
        "quantity": qty,
        "status": "Active" if qty > 0 else "Inactive"
    }
    data["products"].append(product)
    data["next_id"] += 1
    save_data(data)
    print(f"Product '{name}' added successfully with ID {product['id']}.")

def view_products(data):
    print("\n--- All Products ---")
    if not data["products"]:
        print("No products found.")
        return
    print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<10} {'Qty':<8} {'Status'}")
    print("-" * 70)
    for p in data["products"]:
        print(f"{p['id']:<5} {p['name']:<20} {p['category']:<15} {p['price']:<10.2f} {p['quantity']:<8} {p['status']}")

def search_product(data):
    print("\n--- Search Product ---")
    keyword = input("Enter product name or category to search: ").strip().lower()
    if not keyword:
        print("Error: Search keyword cannot be empty.")
        return
    results = [p for p in data["products"] if keyword in p["name"].lower() or keyword in p["category"].lower()]
    if not results:
        print("No matching products found.")
        return
    print(f"\n{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<10} {'Qty':<8} {'Status'}")
    print("-" * 70)
    for p in results:
        print(f"{p['id']:<5} {p['name']:<20} {p['category']:<15} {p['price']:<10.2f} {p['quantity']:<8} {p['status']}")

def update_product(data):
    print("\n--- Update Product ---")
    try:
        pid = int(input("Enter Product ID to update: ").strip())
    except ValueError:
        print("Error: Invalid ID.")
        return

    product = next((p for p in data["products"] if p["id"] == pid), None)
    if not product:
        print(f"Error: Product with ID {pid} not found.")
        return

    print(f"Current: {product['name']} | {product['category']} | Price: {product['price']} | Qty: {product['quantity']}")
    print("(Press Enter to keep current value)")

    name = input(f"New Name [{product['name']}]: ").strip()
    category = input(f"New Category [{product['category']}]: ").strip()
    price = input(f"New Price [{product['price']}]: ").strip()
    qty = input(f"New Quantity [{product['quantity']}]: ").strip()

    if name:
        product["name"] = name
    if category:
        product["category"] = category
    if price:
        try:
            product["price"] = float(price)
        except ValueError:
            print("Invalid price, keeping old value.")
    if qty:
        try:
            product["quantity"] = int(qty)
            product["status"] = "Active" if product["quantity"] > 0 else "Inactive"
        except ValueError:
            print("Invalid quantity, keeping old value.")

    save_data(data)
    print(f"Product ID {pid} updated successfully.")

def delete_product(data):
    print("\n--- Delete Product ---")
    try:
        pid = int(input("Enter Product ID to delete: ").strip())
    except ValueError:
        print("Error: Invalid ID.")
        return

    product = next((p for p in data["products"] if p["id"] == pid), None)
    if not product:
        print(f"Error: Product with ID {pid} not found.")
        return

    confirm = input(f"Are you sure you want to delete '{product['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        data["products"].remove(product)
        save_data(data)
        print(f"Product '{product['name']}' deleted successfully.")
    else:
        print("Delete cancelled.")

def main():
    print("=" * 40)
    print("  Inventory Management System (CLI)")
    print("=" * 40)

    data = load_data()

    while True:
        print("\n--- Main Menu ---")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_product(data)
        elif choice == "2":
            view_products(data)
        elif choice == "3":
            search_product(data)
        elif choice == "4":
            update_product(data)
        elif choice == "5":
            delete_product(data)
        elif choice == "6":
            print("\nThank you for using Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
