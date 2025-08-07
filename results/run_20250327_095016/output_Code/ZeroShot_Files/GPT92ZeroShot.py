import sqlite3

class UserLoginDB:
    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.
        Creates a connection to the SQLite database and ensures the "users" table exists.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        # Create the "users" table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the new user.
        :param password: str, the password of the new user.
        :return: None
        """
        try:
            self.cursor.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return: list of tuples, the rows from the "users" table that match the search criteria.
        """
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchall()

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct.
        :param username: str, the username of the user attempting to log in.
        :param password: str, the password of the user attempting to log in.
        :return: bool, representing whether the user can log in correctly.
        """
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''', (username, password))
        result = self.cursor.fetchone()
        return result is not None

    def __del__(self):
        """
        Ensures that the database connection is closed when the object is destroyed.
        """
        self.connection.close()