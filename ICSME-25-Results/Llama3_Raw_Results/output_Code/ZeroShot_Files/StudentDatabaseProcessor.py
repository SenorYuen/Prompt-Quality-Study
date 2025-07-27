import sqlite3

class StudentDatabaseProcessor:
    def __init__(self, database_name):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(database_name)
        # Create a cursor object
        self.cursor = self.conn.cursor()

    def create_student_table(self):
        # SQL query to create the "students" table
        query = """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                grade INTEGER NOT NULL
            )
        """
        # Execute the query
        self.cursor.execute(query)
        # Commit the changes
        self.conn.commit()

    def insert_student(self, student_data):
        # SQL query to insert a new student into the "students" table
        query = """
            INSERT INTO students (id, name, age, gender, grade)
            VALUES (?, ?, ?, ?, ?)
        """
        # Execute the query with the provided student data
        self.cursor.execute(query, student_data)
        # Commit the changes
        self.conn.commit()

    def search_student_by_name(self, name):
        # SQL query to search for a student by their name
        query = """
            SELECT * FROM students
            WHERE name = ?
        """
        # Execute the query with the provided name
        self.cursor.execute(query, (name,))
        # Fetch all the rows that match the search criteria
        return self.cursor.fetchall()

    def delete_student_by_name(self, name):
        # SQL query to delete a student by their name
        query = """
            DELETE FROM students
            WHERE name = ?
        """
        # Execute the query with the provided name
        self.cursor.execute(query, (name,))
        # Commit the changes
        self.conn.commit()

# Example usage
if __name__ == "__main__":
    processor = StudentDatabaseProcessor("students.db")
    processor.create_student_table()
    
    # Insert a new student
    student_data = (1, "John Doe", 20, "Male", 90)
    processor.insert_student(student_data)
    
    # Search for a student by name
    name = "John Doe"
    result = processor.search_student_by_name(name)
    print(result)
    
    # Delete a student by name
    processor.delete_student_by_name(name)