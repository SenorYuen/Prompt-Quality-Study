import sqlite3

class MovieTicketDB:
    def __init__(self, db_name):
        """
        Initializes the MovieTicketDB object with the specified database name.
        """
        self.db_name = db_name
        # Connect to the database and create the table if it doesn't exist
        self.create_table()

    def create_table(self):
        """
        Creates a "tickets" table in the database if it does not exist already.
        Fields include ID of type int, movie name of type str, theater name of type str,
        seat number of type str, and customer name of type str.
        :return: None
        """
        # Establish connection to the database
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # SQL command to create the tickets table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_name TEXT NOT NULL,
                theater_name TEXT NOT NULL,
                seat_number TEXT NOT NULL,
                customer_name TEXT NOT NULL
            )
        ''')
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        """
        Inserts a new ticket into the "tickets" table.
        :return: None
        """
        # Establish connection to the database
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # SQL command to insert a new ticket
        cursor.execute('''
            INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
            VALUES (?, ?, ?, ?)
        ''', (movie_name, theater_name, seat_number, customer_name))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def search_tickets_by_customer(self, customer_name):
        """
        Searches for tickets in the "tickets" table by customer name.
        :return: list of tuples, the rows from the "tickets" table that match the search criteria.
        """
        # Establish connection to the database
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # SQL command to search for tickets by customer name
        cursor.execute('''
            SELECT * FROM tickets WHERE customer_name = ?
        ''', (customer_name,))
        # Fetch all matching rows
        rows = cursor.fetchall()
        # Close the connection
        conn.close()
        # Return the list of matching rows
        return rows

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket from the "tickets" table by ticket ID.
        :return: None
        """
        # Establish connection to the database
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # SQL command to delete a ticket by ID
        cursor.execute('''
            DELETE FROM tickets WHERE id = ?
        ''', (ticket_id,))
        # Commit the changes and close the connection
        conn.commit()
        conn.close()