from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        # Initialize movies as an empty list
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        # Create a new movie dictionary with given information
        new_movie = {
            'name': name,
            'price': price,
            'start_time': start_time,
            'end_time': end_time,
            # Initialize seats as a 2D array with all zeros
            'seats': np.zeros((n, n))
        }
        # Add the new movie to the list of movies
        self.movies.append(new_movie)

    def book_ticket(self, name, seats_to_book):
        # Find the movie with the given name
        for movie in self.movies:
            if movie['name'] == name:
                # Check if the seats to book are available
                for seat in seats_to_book:
                    if movie['seats'][seat[0], seat[1]] == 1:
                        # If any seat is not available, return booking failed
                        return "Booking failed."
                # If all seats are available, mark them as booked
                for seat in seats_to_book:
                    movie['seats'][seat[0], seat[1]] = 1
                # Return booking success
                return "Booking success."
        # If the movie is not found, return movie not found
        return "Movie not found."

    def available_movies(self, start_time, end_time):
        # Initialize an empty list to store available movie names
        available_movie_names = []
        # Iterate over each movie
        for movie in self.movies:
            # Check if the movie's start time is within the given time range
            if start_time <= movie['start_time'] < end_time:
                # Check if the movie's end time is within the given time range
                if start_time < movie['end_time'] <= end_time:
                    # Add the movie's name to the list of available movie names
                    available_movie_names.append(movie['name'])
        # Return the list of available movie names
        return available_movie_names

# Example usage:
system = MovieBookingSystem()
system.add_movie('Batman', 49.9, datetime(1900, 1, 1, 17, 5), datetime(1900, 1, 1, 19, 25), 3)
print(system.movies)
print(system.book_ticket('Batman', [(0, 0), (0, 1)]))
print(system.book_ticket('Batman', [(0, 0), (0, 1)]))
print(system.available_movies(datetime(1900, 1, 1, 16, 0), datetime(1900, 1, 1, 20, 0)))