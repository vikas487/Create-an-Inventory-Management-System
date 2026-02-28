# Inventory Management System (CLI-Based)

## 🎯 Objective
To develop a simple, lightweight, command-line based Inventory Management System that allows users to perform CRUD (Create, Read, Update, Delete) operations on products with persistent data storage using JSON files.

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3** | Core programming language |
| **JSON** | Data persistence (file-based storage) |

> **Note:** No external libraries or installations are needed. The project uses only Python's built-in `json` module.

## 📂 Project Structure

```
Inventory-Management-System-main/
├── inventory.py      # Main application file (single script)
├── inventory.json    # Auto-generated data storage file
└── README.md         # Project documentation
```

## 🔧 Core Functionality — CRUD Operations

### 1. Create (Add Product)
- User inputs: Product Name, Category, Price, Quantity
- Auto-generates a unique Product ID (auto-incrementing)
- Auto-sets status to "Active" if quantity > 0, otherwise "Inactive"
- Validates inputs (checks for empty name, invalid price/quantity)
- Saves immediately to `inventory.json`

### 2. Read (View All Products)
- Displays all products in a formatted table with columns:
  - ID, Name, Category, Price, Quantity, Status
- Shows "No products found" message if inventory is empty

### 3. Read (Search Product)
- Search by product name or category (case-insensitive)
- Displays matching results in a formatted table
- Supports partial matching (e.g., searching "phone" matches "iPhone")

### 4. Update Product
- User enters Product ID to update
- Shows current values for reference
- Allows updating: Name, Category, Price, Quantity
- Press Enter to skip any field and keep the current value
- Auto-updates status based on new quantity
- Input validation for price (float) and quantity (integer)

### 5. Delete Product
- User enters Product ID to delete
- Shows product name and asks for confirmation (y/n)
- Removes product from inventory upon confirmation
- Saves changes immediately

## 💾 Data Persistence — JSON Storage

### How it works:
- All data is stored in `inventory.json`
- The file is **auto-created** on first run (no setup needed)
- Data is **loaded at startup** and **saved after every change**
- Human-readable format with pretty-printing (4-space indentation)

### JSON Structure:
```json
{
    "products": [
        {
            "id": 1,
            "name": "iPhone",
            "category": "Phone",
            "price": 999.0,
            "quantity": 50,
            "status": "Active"
        }
    ],
    "next_id": 2
}
```

## 🔄 Application Flow

```
Start Program
    ↓
Load data from inventory.json (or create empty data)
    ↓
Display Main Menu (1-6)
    ↓
┌─ 1. Add Product → Input details → Save to JSON
├─ 2. View All → Display formatted table
├─ 3. Search → Input keyword → Show matches
├─ 4. Update → Input ID → Edit fields → Save to JSON
├─ 5. Delete → Input ID → Confirm → Remove → Save to JSON
└─ 6. Exit → End program
    ↓
Loop back to Main Menu (until user chooses Exit)
```

## ✅ Key Features
- **Single file application** — entire system in one Python script
- **No dependencies** — uses only Python's built-in `json` module
- **JSON persistence** — data survives between sessions
- **Input validation** — handles invalid price, quantity, empty inputs
- **Auto-incrementing IDs** — no duplicate product IDs
- **Auto stock status** — marks products Active/Inactive based on quantity
- **Case-insensitive search** — flexible product/category searching
- **Partial matching** — search "lap" finds "Laptop"
- **Safe delete** — confirmation prompt before deleting
- **Skip-field update** — press Enter to keep existing values unchanged

## 💡 Use Cases
- Small retail shops tracking their inventory
- Students learning Python CRUD operations
- Quick inventory tracking for personal use
- Learning JSON file handling in Python

## ▶️ How to Run
```
python inventory.py
```
That's it — no setup, no database, no installations needed!