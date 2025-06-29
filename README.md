# Intro_to_DB - MySQL Database Project

This repository contains a MySQL database schema for an online bookstore and a Python script to create the database.

## Files

- `alx_book_store.sql` - Complete MySQL database schema for the online bookstore
- `MySQLServer.py` - Python script to create the database in MySQL server
- `requirements.txt` - Python dependencies

## Database Schema

The `alx_book_store` database includes the following tables:
- **Authors** - Author information
- **Customers** - Customer information  
- **Books** - Book information with author references
- **Orders** - Order information with customer references
- **Order_Details** - Order details with book and order references

## Setup Instructions

### Prerequisites
- MySQL Server installed and running
- Python 3.x installed
- pip (Python package manager)

### Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure MySQL connection (if needed):**
   Edit `MySQLServer.py` and update the connection parameters:
   ```python
   connection = mysql.connector.connect(
       host="localhost",      # Your MySQL host
       user="root",           # Your MySQL username
       password="",           # Your MySQL password
       port=3306              # Your MySQL port
   )
   ```

3. **Run the database creation script:**
   ```bash
   python3 MySQLServer.py
   ```

4. **Import the database schema (optional):**
   ```bash
   mysql -u root -p alx_book_store < alx_book_store.sql
   ```

## Script Features

- ✅ Creates database if it doesn't exist (won't fail if already exists)
- ✅ Proper error handling for connection issues
- ✅ Automatic connection management (open/close)
- ✅ Success message when database is created
- ✅ No use of SELECT or SHOW statements
- ✅ Clean and readable code structure

## Database Structure

The database follows proper normalization with foreign key relationships:
- Books → Authors (author_id)
- Orders → Customers (customer_id)  
- Order_Details → Orders (order_id)
- Order_Details → Books (book_id) 