import sqlite3

class UserLoginDB:
    """
    This is a database management class for user login verification, providing functions for inserting user information, searching user information, deleting user information, and validating user login.
    """

    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.
        :param db_name: str, the name of the SQLite database.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    # Create a table for storing user information
    def create_table(self):
        # Create table query
        query = """CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )"""
        self.cursor.execute(query)
        self.connection.commit()

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :param username: str, the username of the user.
        :param password: str, the password of the user.
        :return: None
        """
        # Insert user query
        query = """INSERT INTO users (username, password) VALUES (?, ?)"""
        self.cursor.execute(query, (username, password))
        self.connection.commit()

    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return:list of tuples, the rows from the "users" table that match the search criteria.
        """
        # Search user query
        query = """SELECT * FROM users WHERE username = ?"""
        self.cursor.execute(query, (username,))
        return self.cursor.fetchall()

    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :param username: str, the username of the user to delete.
        :return: None
        """
        # Delete user query
        query = """DELETE FROM users WHERE username = ?"""
        self.cursor.execute(query, (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :param username:str, the username of the user to validate.
        :param password:str, the password of the user to validate.
        :return:bool, representing whether the user can log in correctly
        """
        # Validate user login query
        query = """SELECT * FROM users WHERE username = ? AND password = ?"""
        self.cursor.execute(query, (username, password))
        return len(self.cursor.fetchall()) > 0

# Example usage
if __name__ == "__main__":
    user_db = UserLoginDB("user_database.db")
    user_db.create_table()
    user_db.insert_user('user1', 'pass1')
    result = user_db.search_user_by_username('user1')
    print(len(result))  # Output: 1
    user_db.delete_user_by_username('user1')
    print(user_db.validate_user_login('user1', 'pass1'))  # Output: False