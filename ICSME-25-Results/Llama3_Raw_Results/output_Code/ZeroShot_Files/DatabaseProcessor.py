import sqlite3
import pandas as pd

class DatabaseProcessor:

    # Initialize database name of database processor
    def __init__(self, database_name):
        # Connect to SQLite database. It will be created if it doesn't exist.
        self.conn = sqlite3.connect(database_name)
        # Create a cursor object
        self.cursor = self.conn.cursor()


    # Create a new table in the database if it doesn't exist.
    def create_table(self, table_name, key1, key2):
        # SQL query string to create a new table
        query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY,
                {key1} TEXT,
                {key2} INTEGER
            )
        """
        # Execute the query
        self.cursor.execute(query)
        # Commit the changes
        self.conn.commit()


    # Insert data into the specified table in the database.
    def insert_into_database(self, table_name, data):
        # Check if data is a list of tuples
        if not isinstance(data, list) or not all(isinstance(item, tuple) for item in data):
            raise ValueError("Data must be a list of tuples")
        
        # Check if each tuple has exactly 2 elements
        if not all(len(item) == 2 for item in data):
            raise ValueError("Each tuple must have exactly 2 elements")
        
        # SQL query string to insert data into the table
        query = f"""
            INSERT INTO {table_name} ({data[0][0].lower()}, {data[0][1].lower()}) 
            VALUES (?, ?)
        """
        # Execute the query for each tuple in the data
        self.cursor.executemany(query, [(item[1], item[2]) for item in data])
        # Commit the changes
        self.conn.commit()


    # Search the specified table in the database for rows with a matching name.
    def search_database(self, table_name, name):
        # SQL query string to select rows from the table with a matching name
        query = f"""
            SELECT * FROM {table_name} 
            WHERE {table_name[:-1]}1 = ?
        """
        # Execute the query
        self.cursor.execute(query, (name,))
        # Fetch all rows
        rows = self.cursor.fetchall()
        # Return the rows if any, otherwise return None
        return rows if rows else None


    # Delete rows from the specified table in the database with a matching name.
    def delete_from_database(self, table_name, name):
        # SQL query string to delete rows from the table with a matching name
        query = f"""
            DELETE FROM {table_name} 
            WHERE {table_name[:-1]}1 = ?
        """
        # Execute the query
        self.cursor.execute(query, (name,))
        # Commit the changes
        self.conn.commit()


# Example usage
if __name__ == "__main__":
    db = DatabaseProcessor("example.db")
    db.create_table("users", "name", "age")
    data = [("name", "John", 25), ("name", "Alice", 30)]
    db.insert_into_database("users", data)
    print(db.search_database("users", "John"))
    db.delete_from_database("users", "John")
    print(db.search_database("users", "John"))