import sqlite3

class MovieTicketDB:
    def __init__(self, db_name):
        # Initialize the MovieTicketDB object with the specified database name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # Create the "tickets" table if it does not exist already
        self.create_table()

    def create_table(self):
        # Creates a "tickets" table in the database if it does not exist already
        # Fields include ID of type int, movie name of type str, theater name of type str, seat number of type str, and customer name of type str
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             movie_name TEXT, 
             theater_name TEXT, 
             seat_number TEXT, 
             customer_name TEXT)
        ''')
        self.connection.commit()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        # Insert a new ticket into the "tickets" table
        self.cursor.execute('''
            INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
            VALUES (?, ?, ?, ?)
        ''', (movie_name, theater_name, seat_number, customer_name))
        self.connection.commit()

    def search_tickets_by_customer(self, customer_name):
        # Search for tickets in the "tickets" table by customer name
        self.cursor.execute('''
            SELECT * FROM tickets
            WHERE customer_name = ?
        ''', (customer_name,))
        return self.cursor.fetchall()

    def delete_ticket(self, ticket_id):
        # Delete a ticket from the "tickets" table by ticket ID
        self.cursor.execute('''
            DELETE FROM tickets
            WHERE id = ?
        ''', (ticket_id,))
        self.connection.commit()