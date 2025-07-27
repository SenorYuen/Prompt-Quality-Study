from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
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
            'seats': np.zeros((n, n))
        }

        # Add the movie to the list
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        # Find the movie with the given name
        for movie in self.movies:
            if movie['name'] == name:
                # Check if the seats are available
                for seat in seats_to_book:
                    if movie['seats'][seat[0], seat[1]] == 1:
                        return 'Booking failed.'
                # Book the seats
                for seat in seats_to_book:
                    movie['seats'][seat[0], seat[1]] = 1
                return 'Booking success.'
        return 'Movie not found.'

    def available_movies(self, start_time, end_time):
        # Convert time strings to datetime objects
        start_time = datetime.strptime(start_time, '%H:%M')
        start_time = start_time.replace(year=1900, month=1, day=1)
        end_time = datetime.strptime(end_time, '%H:%M')
        end_time = end_time.replace(year=1900, month=1, day=1)

        # Find available movies
        available_movies = [movie['name'] for movie in self.movies 
                            if start_time < movie['end_time'] and end_time > movie['start_time']]
        return available_movies