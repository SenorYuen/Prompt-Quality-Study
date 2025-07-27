import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def create_student_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students
            (ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, gender TEXT, grade INTEGER)
        ''')
        self.conn.commit()

    def insert_student(self, student_data):
        self.cursor.execute('''
            INSERT INTO students (name, age, gender, grade)
            VALUES (?, ?, ?, ?)
        ''', (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
        self.conn.commit()

    def search_student_by_name(self, name):
        self.cursor.execute('''
            SELECT * FROM students
            WHERE name = ?
        ''', (name,))
        return self.cursor.fetchall()

    def delete_student_by_name(self, name):
        self.cursor.execute('''
            DELETE FROM students
            WHERE name = ?
        ''', (name,))
        self.conn.commit()