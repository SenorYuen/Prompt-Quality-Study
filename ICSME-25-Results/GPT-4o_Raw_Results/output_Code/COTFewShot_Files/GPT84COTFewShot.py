import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    gender TEXT,
                    grade INTEGER
                )
            ''')
            conn.commit()
        finally:
            conn.close()

    def insert_student(self, student_data):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, age, gender, grade)
                VALUES (?, ?, ?, ?)
            ''', (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
            conn.commit()
        finally:
            conn.close()

    def search_student_by_name(self, name):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM students WHERE name = ?
            ''', (name,))
            results = cursor.fetchall()
            return results
        finally:
            conn.close()

    def delete_student_by_name(self, name):
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM students WHERE name = ?
            ''', (name,))
            conn.commit()
        finally:
            conn.close()