from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    This is a class for a movie booking system, which allows adding movies, booking tickets, and checking the available movies within a given time range.
    """

    def __init__(self):
        """
        Initialize movies containing the information about movies.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies.
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats (n*n)
        """
        # Convert start and end times from string to datetime objects
        start_dt = datetime.strptime(start_time, '%H:%M')
        end_dt = datetime.strptime(end_time, '%H:%M')
        
        # Initialize the seating arrangement as a numpy array of zeros
        seats = np.zeros((n, n))

        # Add the movie details to the movies list
        self.movies.append({
            'name': name,
            'price': price,
            'start_time': start_dt,
            'end_time': end_dt,
            'seats': seats
        })

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if booked successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message.
        """
        # Search for the movie by name
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                # Check if all requested seats are available
                if all(movie['seats'][row, col] == 0 for row, col in seats_to_book):
                    # Mark the requested seats as booked
                    for row, col in seats_to_book:
                        movie['seats'][row, col] = 1
                    return 'Booking success.'
                else:
                    return 'Booking failed.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range.
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        """
        # Convert start and end times from string to datetime objects
        start_dt = datetime.strptime(start_time, '%H:%M')
        end_dt = datetime.strptime(end_time, '%H:%M')

        # List to hold available movie names
        available_movies = []

        # Check each movie's schedule against the provided time range
        for movie in self.movies:
            if movie['start_time'] >= start_dt and movie['end_time'] <= end_dt:
                available_movies.append(movie['name'])

        return available_movies