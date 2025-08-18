'''
# This is a database management class for user login verification, providing functions for inserting user information, searching user information, deleting user information, and validating user login.

class UserLoginDB:
    def __init__(self, db_name):
        """
        Initializes the UserLoginDB object with the specified database name.

        """

    def insert_user(self, username, password):
        """
        Inserts a new user into the "users" table.
        :return: None
        """


    def search_user_by_username(self, username):
        """
        Searches for users in the "users" table by username.
        :param username: str, the username of the user to search for.
        :return:list of tuples, the rows from the "users" table that match the search criteria.
        """


    def delete_user_by_username(self, username):
        """
        Deletes a user from the "users" table by username.
        :return: None
        """


    def validate_user_login(self, username, password):
        """
        Determine whether the user can log in, that is, the user is in the database and the password is correct
        :return:bool, representing whether the user can log in correctly
        """
'''

import sqlite3


class UserLoginDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def insert_user(self, username, password):
        self.cursor.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', (username, password))
        self.connection.commit()

    def search_user_by_username(self, username):
        self.cursor.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,))
        user = self.cursor.fetchone()
        return user

    def delete_user_by_username(self, username):
        self.cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        self.connection.commit()

    def validate_user_login(self, username, password):
        user = self.search_user_by_username(username)
        if user is not None and user[1] == password:
            return True
        return False

