import sqlite3
import pandas as pd

class DatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY,
                        {key1} TEXT,
                        {key2} INTEGER
                    )
                """)
            return True
        except:
            return False

    def insert_into_database(self, table_name, data):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                for row in data:
                    cursor.execute(f"""
                        INSERT INTO {table_name} ({list(row.keys())[0]}, {list(row.keys())[1]})
                        VALUES (?, ?)
                    """, (row[list(row.keys())[0]], row[list(row.keys())[1]]))
            return True
        except:
            return False

    def search_database(self, table_name, name):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f"""
                    SELECT * FROM {table_name}
                    WHERE {list(pd.read_sql_query(f"PRAGMA table_info({table_name})", conn).iloc[1]['name'])} = ?
                """, (name,))
                return cursor.fetchall()
        except:
            return []

    def delete_from_database(self, table_name, name):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f"""
                    DELETE FROM {table_name}
                    WHERE {list(pd.read_sql_query(f"PRAGMA table_info({table_name})", conn).iloc[1]['name'])} = ?
                """, (name,))
            return True
        except:
            return False