# advanced-inventory
## User Story:
As a small business owner, I want to manage my inventory digitally and store it in external files, so that I can avoid losing information when closing the program, analyze my sales performance, and easily share my data

## System Features

The system includes the following functionalities:

## Register customers
Store customer information including:
ID
Name
Email
📦 Register products
Store product information including:
ID
Name
Price
🛒 Create orders
Link a customer with:
Product
Quantity
📋 View registered orders
Display all saved orders.
💰 Calculate total daily income
Automatically calculate total sales income.
📊 Generate final report
Show a summary of:
Total sales
Orders
Products sold

 ##Technical Approach

This project was built using:

Dictionaries 🧾
Used to store:
Customers
Orders
Tuples 📦
Used to store product data because:
They are immutable
They help protect product information
## Code Structure

The system follows a modular structure using reusable functions.

Each function:

Receives parameters
Returns values
Avoids direct printing inside the logic
Keeps the code clean and reusable

This structure improves:

Code readability
Maintenance
Scalability
## System Output

At the end of execution, the system generates:

📋 Total number of orders
💰 Total income
👥 Orders grouped by customer
📦 List of products sold
<img width="3337" height="2871" alt="advance inventory drawio (1)" src="https://github.com/user-attachments/assets/ffc3f4c4-31a9-4d84-9b15-507c9c695687" />
