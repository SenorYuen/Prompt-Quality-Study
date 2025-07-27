import sqlite3

class BookManagementDB:

    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection and cursor, 
        and creates the book table if it does not already exist
        """
        self.conn = sqlite3.connect(db_name)  # Connect to the database
        self.cursor = self.conn.cursor()  # Create a cursor object
        self.create_table()  # Ensure the book table exists

    def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                available INTEGER NOT NULL
            )
        """)
        self.conn.commit()  # Save the changes

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        """
        self.cursor.execute("""
            INSERT INTO books (title, author, available) 
            VALUES (?, ?, 1)
        """, (title, author))
        self.conn.commit()  # Save the changes

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        """
        self.cursor.execute("""
            DELETE FROM books WHERE id = ?
        """, (book_id,))
        self.conn.commit()  # Save the changes

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        """
        self.cursor.execute("""
            UPDATE books SET available = 0 WHERE id = ?
        """, (book_id,))
        self.conn.commit()  # Save the changes

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        """
        self.cursor.execute("""
            UPDATE books SET available = 1 WHERE id = ?
        """, (book_id,))
        self.conn.commit()  # Save the changes

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        return books: list[tuple], the information of all books in database
        """
        self.cursor.execute("""
            SELECT * FROM books
        """)
        books = self.cursor.fetchall()  # Fetch all results
        return books  # Return the list of books