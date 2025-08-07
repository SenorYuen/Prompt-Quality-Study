'''
# This is a class with database operation, including inserting student information, searching for student information by name, and deleting student information by name.

import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        """
    

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        """

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :return: None
        """

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :return: None
        """
'''

import sqlite3


class StudentDatabaseProcessor:

    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
        """
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()

    def insert_student(self, student_data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO students (name, age, gender, grade)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query,
                       (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))

        conn.commit()
        conn.close()

    def search_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        select_query = "SELECT * FROM students WHERE name = ?"
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()

        conn.close()

        return result

    def delete_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        delete_query = "DELETE FROM students WHERE name = ?"
        cursor.execute(delete_query, (name,))

        conn.commit()
        conn.close()


