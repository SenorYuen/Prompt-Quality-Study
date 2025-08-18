'''
# This is a class for movie database operations, which allows for inserting movie information, searching for movie information by name, and deleting movie information by name.

import sqlite3

class MovieTicketDB:
    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        """


    def create_table(self):
        """
        Creates a "tickets" table in the database if it does not exist already.Fields include ID of type int, movie name of type str, theater name of type str, seat number of type str, and customer name of type str
        :return: None
        """

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :return: None
        """

    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        """

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :return: None
        """

'''

import sqlite3


class MovieTicketDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY,
                movie_name TEXT,
                theater_name TEXT,
                seat_number TEXT,
                customer_name TEXT
            )
        ''')
        self.connection.commit()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        self.cursor.execute('''
            INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
            VALUES (?, ?, ?, ?)
        ''', (movie_name, theater_name, seat_number, customer_name))
        self.connection.commit()

    def search_tickets_by_customer(self, customer_name):
        self.cursor.execute('''
            SELECT * FROM tickets WHERE customer_name = ?
        ''', (customer_name,))
        tickets = self.cursor.fetchall()
        return tickets

    def delete_ticket(self, ticket_id):
        self.cursor.execute('''
            DELETE FROM tickets WHERE id = ?
        ''', (ticket_id,))
        self.connection.commit()


