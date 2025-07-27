import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    grade INTEGER NOT NULL
                )
            ''')
            conn.commit()

    def insert_student(self, student_data):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, age, gender, grade)
                VALUES (:name, :age, :gender, :grade)
            ''', student_data)
            conn.commit()

    def search_student_by_name(self, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM students WHERE name = ?
            ''', (name,))
            return cursor.fetchall()

    def delete_student_by_name(self, name):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM students WHERE name = ?
            ''', (name,))
            conn.commit()