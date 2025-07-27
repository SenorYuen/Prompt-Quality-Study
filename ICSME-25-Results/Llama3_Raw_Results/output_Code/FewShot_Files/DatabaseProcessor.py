import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """

    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name
        # Connect to the SQLite database
        self.conn = sqlite3.connect(self.database_name)
        # Create a cursor object
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        """
        # SQL query to create a new table
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

    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        """
        # SQL query to insert data into the table
        query = f"""
            INSERT INTO {table_name} ({list(data[0].keys())[0]}, {list(data[0].keys())[1]})
            VALUES (?, ?)
        """
        # Execute the query for each row of data
        for row in data:
            self.cursor.execute(query, (row[list(row.keys())[0]], row[list(row.keys())[1]]))
        # Commit the changes
        self.conn.commit()

    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        """
        # SQL query to search for rows with a matching name
        query = f"""
            SELECT * FROM {table_name} WHERE {list(self.get_columns(table_name))[0]} = ?
        """
        # Execute the query
        self.cursor.execute(query, (name,))
        # Fetch all the rows
        rows = self.cursor.fetchall()
        # Return the rows if any, otherwise return None
        return rows if rows else None

    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        """
        # SQL query to delete rows with a matching name
        query = f"""
            DELETE FROM {table_name} WHERE {list(self.get_columns(table_name))[0]} = ?
        """
        # Execute the query
        self.cursor.execute(query, (name,))
        # Commit the changes
        self.conn.commit()

    def get_columns(self, table_name):
        # SQL query to get the column names
        query = f"""
            PRAGMA table_info({table_name})
        """
        # Execute the query
        self.cursor.execute(query)
        # Fetch all the rows
        rows = self.cursor.fetchall()
        # Return a list of column names
        return [row[1] for row in rows]

    def close_connection(self):
        # Close the connection
        self.conn.close()