#!/usr/bin/env python3
"""
MySQL Database Creation Script
Creates the alx_book_store database in MySQL server
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Creates the alx_book_store database in MySQL server
    """
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3306
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            
            # Commit the changes
            connection.commit()
            
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close database connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database() 