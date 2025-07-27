from datetime import datetime
import numpy as np

class MovieBookingSystem:
    """
    this is a class as movie booking system, which allows to add movies, book tickets and check the available movies within a given time range. 
    """

    def __init__(self):
        """
        Initialize movies contains the information about movies
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies
        :param name: str, movie name
        :param price: float, price for one ticket
        :param start_time: str
        :param end_time: str
        :param n: int, the size of seats(n*n)
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.movies
        [{'name': 'Batman', 'price': 49.9, 'start_time': datetime.datetime(1900, 1, 1, 17, 5), 'end_time': datetime.datetime(1900, 1, 1, 19, 25),
        'seats': array([[0., 0., 0.],
            [0., 0., 0.],
            [0., 0., 0.]])}]
        """
        # Convert time strings to datetime objects
        start_time = datetime.strptime(start_time, '%H:%M')
        start_time = start_time.replace(year=1900, month=1, day=1)
        end_time = datetime.strptime(end_time, '%H:%M')
        end_time = end_time.replace(year=1900, month=1, day=1)
        
        # Create a new movie dictionary
        movie = {
            'name': name,
            'price': price,
            'start_time': start_time,
            'end_time': end_time,
            'seats': np.zeros((n, n))  # Initialize seats as a 2D numpy array
        }
        
        # Add the movie to the list
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Change the seats value in self.movies if book successfully.
        :param name: str, movie name
        :param seats_to_book: list of tuples, representing seats to book [(row1, col1), (row2, col2), ...]
        :return: str, booking status message. "Movie not found." for no such movie.
                "Booking success." for successfully booking, or "Booking failed." otherwise
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.book_ticket('Batman', [(0, 0), (0, 1)])
        'Booking success.'
        >>> system.book_ticket('Batman', [(0, 0)])
        'Booking failed.'
        >>> system.book_ticket('batman', [(0, 0)])
        'Movie not found.'
        """
        # Find the movie
        movie = next((m for m in self.movies if m['name'] == name), None)
        
        # Check if movie exists
        if movie is None:
            return "Movie not found."
        
        # Check if seats are available
        for seat in seats_to_book:
            if movie['seats'][seat[0], seat[1]] == 1:
                return "Booking failed."
        
        # Book the seats
        for seat in seats_to_book:
            movie['seats'][seat[0], seat[1]] = 1
        
        return "Booking success."

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range
        :param start_time: str, start time in HH:MM format
        :param end_time: str, end time in HH:MM format
        :return: list of str, names of available movies
        >>> system.add_movie('Batman', 49.9, '17:05', '19:25', 3)
        >>> system.available_movies('12:00', '22:00')
        ['Batman']
        """
        # Convert time strings to datetime objects
        start_time = datetime.strptime(start_time, '%H:%M')
        start_time = start_time.replace(year=1900, month=1, day=1)
        end_time = datetime.strptime(end_time, '%H:%M')
        end_time = end_time.replace(year=1900, month=1, day=1)
        
        # Find available movies
        available_movies = [m['name'] for m in self.movies if start_time < m['end_time'] and end_time > m['start_time']]
        
        return available_movies