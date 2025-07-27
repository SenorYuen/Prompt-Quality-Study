import sqlite3
import pandas as pd

class DatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_table(self, table_name, key1, key2):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY,
                {key1} TEXT,
                {key2} INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def insert_into_database(self, table_name, data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        for row in data:
            keys = ', '.join(row.keys())
            placeholders = ', '.join('?' * len(row))
            values = tuple(row.values())
            cursor.execute(f'''
                INSERT INTO {table_name} ({keys})
                VALUES ({placeholders})
            ''', values)
        conn.commit()
        conn.close()

    def search_database(self, table_name, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f'''
            SELECT * FROM {table_name} WHERE name = ?
        ''', (name,))
        results = cursor.fetchall()
        conn.close()
        return results

    def delete_from_database(self, table_name, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f'''
            DELETE FROM {table_name} WHERE name = ?
        ''', (name,))
        conn.commit()
        conn.close()