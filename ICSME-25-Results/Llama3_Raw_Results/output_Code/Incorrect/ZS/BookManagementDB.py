import sqlite3

class BookManagementDB:

    def __init__(self, db_name):
        # Create a database connection
        self.conn = sqlite3.connect(db_name)
        # Create a cursor object
        self.cursor = self.conn.cursor()
        # Create the book table if it does not already exist
        self.create_table()

    def create_table(self):
        # SQL query to create the book table
        query = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                available INTEGER DEFAULT 1
            )
        """
        # Execute the query
        self.cursor.execute(query)
        # Commit the changes
        self.conn.commit()

    def add_book(self, title, author):
        # SQL query to insert a new book into the table
        query = """
            INSERT INTO books (title, author)
            VALUES (?, ?)
        """
        # Execute the query with the provided title and author
        self.cursor.execute(query, (title, author))
        # Commit the changes
        self.conn.commit()

    def remove_book(self, book_id):
        # SQL query to delete a book from the table based on the book ID
        query = """
            DELETE FROM books
            WHERE id = ?
        """
        # Execute the query with the provided book ID
        self.cursor.execute(query, (book_id,))
        # Commit the changes
        self.conn.commit()

    def borrow_book(self, book_id):
        # SQL query to update the availability of a book to 0 (borrowed)
        query = """
            UPDATE books
            SET available = 0
            WHERE id = ? AND available = 1
        """
        # Execute the query with the provided book ID
        self.cursor.execute(query, (book_id,))
        # Commit the changes
        self.conn.commit()

    def return_book(self, book_id):
        # SQL query to update the availability of a book to 1 (available)
        query = """
            UPDATE books
            SET available = 1
            WHERE id = ? AND available = 0
        """
        # Execute the query with the provided book ID
        self.cursor.execute(query, (book_id,))
        # Commit the changes
        self.conn.commit()

    def search_books(self):
        # SQL query to select all books from the table
        query = """
            SELECT *
            FROM books
        """
        # Execute the query
        self.cursor.execute(query)
        # Fetch all the rows from the query
        books = self.cursor.fetchall()
        # Return the list of books
        return books

# Example usage:
if __name__ == "__main__":
    db = BookManagementDB("book_management.db")
    db.add_book("To Kill a Mockingbird", "Harper Lee")
    db.add_book("1984", "George Orwell")
    print(db.search_books())
    db.borrow_book(1)
    print(db.search_books())
    db.return_book(1)
    print(db.search_books())
    db.remove_book(2)
    print(db.search_books())