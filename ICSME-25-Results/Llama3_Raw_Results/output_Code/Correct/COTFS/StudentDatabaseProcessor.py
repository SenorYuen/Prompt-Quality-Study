import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL,
                        grade INTEGER NOT NULL
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_student(self, student_data):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO students (name, age, gender, grade)
                    VALUES (?, ?, ?, ?)
                ''', (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting student: {e}")

    def search_student_by_name(self, name):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM students
                    WHERE name = ?
                ''', (name,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error searching student: {e}")
            return []

    def delete_student_by_name(self, name):
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM students
                    WHERE name = ?
                ''', (name,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting student: {e}")