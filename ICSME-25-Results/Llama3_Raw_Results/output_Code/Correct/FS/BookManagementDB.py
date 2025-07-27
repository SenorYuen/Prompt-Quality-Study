import sqlite3

class BookManagementDB:
    """
    This is a database class as a book management system, used to handle the operations of adding, removing, updating, and searching books.
    """

    def __init__(self, db_name):
        """
        Initializes the class by creating a database connection and cursor, 
        and creates the book table if it does not already exist
        :param db_name: str, the name of db file
        """
        # Create a connection to the SQLite database
        self.connection = sqlite3.connect(db_name)
        # Create a cursor object to execute SQL queries
        self.cursor = self.connection.cursor()
        # Create the book table if it does not already exist
        self.create_table()

    def create_table(self):
        """
        Creates the book table in the database if it does not already exist.
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
        # SQL query to create the book table
        query = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            )
        """
        # Execute the SQL query
        self.cursor.execute(query)
        # Commit the changes to the database
        self.connection.commit()

    def add_book(self, title, author):
        """
        Adds a book to the database with the specified title and author, 
        setting its availability to 1 as free to borrow.
        :param title: str, book title
        :param author: str, author name
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        >>> book_db.add_book('book1', 'author')
        """
        # SQL query to insert a new book into the book table
        query = "INSERT INTO books (title, author) VALUES (?, ?)"
        # Execute the SQL query with the provided title and author
        self.cursor.execute(query, (title, author))
        # Commit the changes to the database
        self.connection.commit()

    def remove_book(self, book_id):
        """
        Removes a book from the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
        # SQL query to delete a book from the book table
        query = "DELETE FROM books WHERE id = ?"
        # Execute the SQL query with the provided book ID
        self.cursor.execute(query, (book_id,))
        # Commit the changes to the database
        self.connection.commit()

    def borrow_book(self, book_id):
        """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
        # SQL query to update the availability of a book in the book table
        query = "UPDATE books SET available = 0 WHERE id = ?"
        # Execute the SQL query with the provided book ID
        self.cursor.execute(query, (book_id,))
        # Commit the changes to the database
        self.connection.commit()

    def return_book(self, book_id):
        """
        Marks a book as returned in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
        # SQL query to update the availability of a book in the book table
        query = "UPDATE books SET available = 1 WHERE id = ?"
        # Execute the SQL query with the provided book ID
        self.cursor.execute(query, (book_id,))
        # Commit the changes to the database
        self.connection.commit()

    def search_books(self):
        """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
        # SQL query to select all books from the book table
        query = "SELECT * FROM books"
        # Execute the SQL query
        self.cursor.execute(query)
        # Fetch all the rows from the query result
        rows = self.cursor.fetchall()
        # Return the list of books
        return rows