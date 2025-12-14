import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (no database yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',        # Replace with your MySQL username
        password=''         # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
