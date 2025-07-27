import sqlite3

class MovieTicketDB:
    def __init__(self, db_name):
        # Connect to the SQLite database
        self.conn = sqlite3.connect(db_name)
        # Create a cursor object
        self.cursor = self.conn.cursor()

    def create_table(self):
        # SQL query to create the "tickets" table
        query = """
            CREATE TABLE IF NOT EXISTS tickets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_name TEXT,
                theater_name TEXT,
                seat_number TEXT,
                customer_name TEXT
            )
        """
        # Execute the query
        self.cursor.execute(query)
        # Commit the changes
        self.conn.commit()

    def insert_ticket(self, movie_name, theater_name, seat_number, customer_name):
        # SQL query to insert a new ticket into the "tickets" table
        query = """
            INSERT INTO tickets (movie_name, theater_name, seat_number, customer_name)
            VALUES (?, ?, ?, ?)
        """
        # Execute the query with the provided values
        self.cursor.execute(query, (movie_name, theater_name, seat_number, customer_name))
        # Commit the changes
        self.conn.commit()

    def search_tickets_by_customer(self, customer_name):
        # SQL query to search for tickets by customer name
        query = """
            SELECT * FROM tickets
            WHERE customer_name = ?
        """
        # Execute the query with the provided customer name
        self.cursor.execute(query, (customer_name,))
        # Fetch all the rows that match the search criteria
        rows = self.cursor.fetchall()
        # Return the rows
        return rows

    def delete_ticket(self, ticket_id):
        # SQL query to delete a ticket by ticket ID
        query = """
            DELETE FROM tickets
            WHERE id = ?
        """
        # Execute the query with the provided ticket ID
        self.cursor.execute(query, (ticket_id,))
        # Commit the changes
        self.conn.commit()

# Example usage:
if __name__ == "__main__":
    db = MovieTicketDB("movie_tickets.db")
    db.create_table()
    db.insert_ticket("Movie 1", "Theater 1", "A1", "John Doe")
    db.insert_ticket("Movie 2", "Theater 2", "B2", "Jane Doe")
    print(db.search_tickets_by_customer("John Doe"))
    db.delete_ticket(1)
    print(db.search_tickets_by_customer("John Doe"))