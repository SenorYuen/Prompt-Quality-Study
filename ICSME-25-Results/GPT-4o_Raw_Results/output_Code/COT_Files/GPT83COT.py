import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                grade INTEGER
            )
        ''')
        connection.commit()
        connection.close()

    def insert_student(self, student_data):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO students (name, age, gender, grade) 
            VALUES (:name, :age, :gender, :grade)
        ''', student_data)
        connection.commit()
        connection.close()

    def search_student_by_name(self, name):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM students WHERE name = ?
        ''', (name,))
        rows = cursor.fetchall()
        connection.close()
        return rows

    def delete_student_by_name(self, name):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        cursor.execute('''
            DELETE FROM students WHERE name = ?
        ''', (name,))
        connection.commit()
        connection.close()