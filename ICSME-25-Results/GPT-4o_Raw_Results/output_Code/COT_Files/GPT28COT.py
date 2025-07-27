import sqlite3
import pandas as pd

class DatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY,
                    {key1} TEXT,
                    {key2} INTEGER
                )
            ''')
            conn.commit()

    def insert_into_database(self, table_name, data):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            for row in data:
                columns = ', '.join(row.keys())
                placeholders = ', '.join('?' * len(row))
                values = tuple(row.values())
                cursor.execute(f'''
                    INSERT INTO {table_name} ({columns})
                    VALUES ({placeholders})
                ''', values)
            conn.commit()

    def search_database(self, table_name, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                SELECT * FROM {table_name}
                WHERE name = ?
            ''', (name,))
            return cursor.fetchall()

    def delete_from_database(self, table_name, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                DELETE FROM {table_name}
                WHERE name = ?
            ''', (name,))
            conn.commit()