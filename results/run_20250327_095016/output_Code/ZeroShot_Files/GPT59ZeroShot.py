from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        """
        Initialize the movie booking system with an empty list of movies.
        Each movie is represented as a dictionary containing its name, price, start and end times, and a seating chart.
        """
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        """
        Add a new movie into self.movies.
        
        :param name: str, name of the movie
        :param price: float, price of a ticket
        :param start_time: datetime, start time of the movie
        :param end_time: datetime, end time of the movie
        :param n: int, dimension of the seating chart (n x n)
        """
        movie = {
            'name': name,
            'price': price,
            'start_time': start_time,
            'end_time': end_time,
            'seats': np.zeros((n, n))
        }
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        """
        Book tickets for a movie. Update the seats in self.movies if booking is successful.
        
        :param name: str, name of the movie to book
        :param seats_to_book: list of tuples, each tuple contains row and column index of seat to book
        :return: str, booking status message
        """
        for movie in self.movies:
            if movie['name'] == name:
                for row, col in seats_to_book:
                    if movie['seats'][row][col] == 0:
                        movie['seats'][row][col] = 1
                    else:
                        return "Booking failed."
                return "Booking success."
        return "Movie not found."

    def available_movies(self, start_time, end_time):
        """
        Get a list of available movies within the specified time range.
        
        :param start_time: datetime, start of the time range
        :param end_time: datetime, end of the time range
        :return: list of str, names of available movies
        """
        available = []
        for movie in self.movies:
            if movie['start_time'] >= start_time and movie['end_time'] <= end_time:
                available.append(movie['name'])
        return available