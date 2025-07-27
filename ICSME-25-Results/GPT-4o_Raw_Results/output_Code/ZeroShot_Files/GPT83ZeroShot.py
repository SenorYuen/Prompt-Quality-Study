import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        """
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.
        Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: tuple containing (name, age, gender, grade)
        :return: None
        """
        insert_query = """
        INSERT INTO students (name, age, gender, grade)
        VALUES (?, ?, ?, ?);
        """
        self.cursor.execute(insert_query, student_data)
        self.connection.commit()

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, name of the student to search for
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """
        search_query = """
        SELECT * FROM students WHERE name = ?;
        """
        self.cursor.execute(search_query, (name,))
        return self.cursor.fetchall()

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, name of the student to delete
        :return: None
        """
        delete_query = """
        DELETE FROM students WHERE name = ?;
        """
        self.cursor.execute(delete_query, (name,))
        self.connection.commit()

    def __del__(self):
        """
        Destructor to close the database connection when the object is deleted.
        """
        self.connection.close()