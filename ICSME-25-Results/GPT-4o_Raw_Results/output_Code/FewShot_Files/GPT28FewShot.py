import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, 
    insert data into the database, search for data based on name, 
    and delete data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize database name of the database processor
        """
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        Make id (INTEGER) as PRIMARY KEY, key1 as TEXT, key2 as INTEGER
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        # Create table with specified columns
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {key1} TEXT,
                {key2} INTEGER
            )
        ''')
        
        # Commit changes and close connection
        conn.commit()
        conn.close()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        # Insert data into the table
        for item in data:
            cursor.execute(f'''
                INSERT INTO {table_name} ({", ".join(item.keys())})
                VALUES ({", ".join(['?' for _ in item.values()])})
            ''', tuple(item.values()))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        # Search for rows with the specified name
        cursor.execute(f'''
            SELECT * FROM {table_name} WHERE name = ?
        ''', (name,))
        
        # Fetch all matching rows
        results = cursor.fetchall()
        
        # Close connection
        conn.close()
        
        return results if results else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        # Delete rows with the specified name
        cursor.execute(f'''
            DELETE FROM {table_name} WHERE name = ?
        ''', (name,))
        
        # Commit changes and close connection
        conn.commit()
        conn.close()