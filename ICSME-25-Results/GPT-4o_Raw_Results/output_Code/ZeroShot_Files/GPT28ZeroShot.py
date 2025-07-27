import sqlite3
import pandas as pd

class DatabaseProcessor:

    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name
        # Connect to the database
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        """
        # SQL command to create a table with id as PRIMARY KEY, key1 as TEXT, and key2 as INTEGER
        create_table_sql = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {key1} TEXT,
            {key2} INTEGER
        );
        '''
        # Execute the SQL command
        self.cursor.execute(create_table_sql)
        # Commit changes
        self.connection.commit()

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        """
        # Assuming data is a list of dictionaries with keys matching table columns
        keys = data[0].keys()
        columns = ', '.join(keys)
        placeholders = ', '.join('?' for _ in keys)
        insert_sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'

        # Insert each row of data
        for row in data:
            values = tuple(row[key] for key in keys)
            self.cursor.execute(insert_sql, values)
        
        # Commit changes
        self.connection.commit()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        """
        # SQL command to search for rows with a matching name
        search_sql = f'SELECT * FROM {table_name} WHERE name = ?'
        self.cursor.execute(search_sql, (name,))
        # Fetch all matching rows
        results = self.cursor.fetchall()
        return results if results else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        """
        # SQL command to delete rows with a matching name
        delete_sql = f'DELETE FROM {table_name} WHERE name = ?'
        self.cursor.execute(delete_sql, (name,))
        # Commit changes
        self.connection.commit()

    def __del__(self):
        """
        Destructor to close the database connection when the object is deleted
        """
        self.connection.close()