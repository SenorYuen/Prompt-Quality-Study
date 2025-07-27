import sqlite3
import pandas as pd

class DatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, key1, key2):
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY,
                {key1} TEXT,
                {key2} INTEGER
            )
        """)
        self.conn.commit()

    def insert_into_database(self, table_name, data):
        for row in data:
            self.cursor.execute(f"""
                INSERT INTO {table_name} ({list(row.keys())[0]}, {list(row.keys())[1]})
                VALUES (?, ?)
            """, (row[list(row.keys())[0]], row[list(row.keys())[1]]))
        self.conn.commit()

    def search_database(self, table_name, name):
        self.cursor.execute(f"""
            SELECT * FROM {table_name}
            WHERE {list({'name': 'name', 'age': 'age'}.keys())[0]} = ?
        """, (name,))
        return self.cursor.fetchall()

    def delete_from_database(self, table_name, name):
        self.cursor.execute(f"""
            DELETE FROM {table_name}
            WHERE {list({'name': 'name', 'age': 'age'}.keys())[0]} = ?
        """, (name,))
        self.conn.commit()