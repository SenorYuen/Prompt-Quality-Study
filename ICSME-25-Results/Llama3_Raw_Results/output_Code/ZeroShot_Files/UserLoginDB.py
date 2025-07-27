import sqlite3

class UserLoginDB:
    def __init__(self, db_name):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_name)
        # Create a cursor object
        self.cursor = self.conn.cursor()
        # Create the "users" table if it does not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (username TEXT PRIMARY KEY, password TEXT)
        ''')
        # Commit the transaction
        self.conn.commit()

    def insert_user(self, username, password):
        # Insert a new user into the "users" table
        self.cursor.execute('INSERT INTO users VALUES (?, ?)', (username, password))
        # Commit the transaction
        self.conn.commit()

    def search_user_by_username(self, username):
        # Search for users in the "users" table by username
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        # Fetch all rows from the last executed statement
        return self.cursor.fetchall()

    def delete_user_by_username(self, username):
        # Delete a user from the "users" table by username
        self.cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        # Commit the transaction
        self.conn.commit()

    def validate_user_login(self, username, password):
        # Search for the user in the "users" table
        self.cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        # Fetch the row from the last executed statement
        user = self.cursor.fetchone()
        # Check if the user exists and the password is correct
        if user and user[1] == password:
            return True
        else:
            return False

    # Close the connection when the object is destroyed
    def __del__(self):
        self.conn.close()