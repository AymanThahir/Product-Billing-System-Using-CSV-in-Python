# 🧾 Receipt Generator (S-Mart Shopping CLI)

A simple command-line Python tool for managing a mini shopping system. Add products to inventory, generate bills based on selected items, and save output as a CSV receipt. Perfect for beginners learning file handling, CSV operations, and basic input/output logic.

---

## 📌 Features

- Add new products to the inventory (`products.csv`)
- Retrieve product details by Product ID (PID)
- Interactive billing system for customers
- CSV receipt generation with product, quantity, and total price
- Calculates and displays the total bill

---

## 🧰 Technologies Used

- **Python 3**
- **CSV Module** – For reading/writing `.csv` files

---

## 🧑‍💻 How It Works

### Main Functionalities:
1. **Add Inventory**  
   Add multiple items with PID, name, and price to the inventory file.

2. **Billing**  
   - Input Product ID and quantity.
   - Look up the product.
   - Append it to a virtual bill.
   - Generate a CSV receipt (`bill.csv`) with totals.

---

## 💡 Usage

### 1. Clone the Repository

git clone https://github.com/yourusername/receipt-generator.git
cd receipt-generator

### 2. Run the Program


python receipt.py

You’ll see a menu with two options:

* Press `1` to start billing.
* Press `2` to add new products to inventory.


## 📁 File Structure

receipt-generator/
│
├── receipt.py         # Main Python script
├── products.csv       # Stores all product info
├── bill.csv           # Output receipt file (auto-generated)
└── README.md          # Project documentation

---

## 📘 Sample CSV Format

### `products.csv`

| PID  | Name   | Price |
| ---- | ------ | ----- |
| P001 | Mango  | 50    |
| P002 | Banana | 30    |

### `bill.csv`

| PID  | Product\_Name | Price | Quantity | Total |
| ---- | ------------- | ----- | -------- | ----- |
| P001 | Mango         | 50    | 2        | 100   |
| P002 | Banana        | 30    | 3        | 90    |
|      |               |       | TOTAL:   | 190   |

---

## ✅ Requirements

* Python 3.x
* No external dependencies

---
