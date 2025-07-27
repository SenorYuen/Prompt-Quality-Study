from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        # Initialize an empty list to store movie information
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        # Convert start_time and end_time to datetime format
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
        
        # Add the new movie to the list
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        # Find the movie with the given name
        for movie in self.movies:
            if movie['name'] == name:
                # Check if the seats are available
                for seat in seats_to_book:
                    row, col = seat
                    if movie['seats'][row, col] == 1:
                        return "Booking failed."
                
                # Book the seats
                for seat in seats_to_book:
                    row, col = seat
                    movie['seats'][row, col] = 1
                
                return "Booking success."
        
        # If the movie is not found
        return "Movie not found."

    def available_movies(self, start_time, end_time):
        # Convert start_time and end_time to datetime format
        start_time = datetime.strptime(start_time, '%H:%M')
        start_time = start_time.replace(year=1900, month=1, day=1)
        end_time = datetime.strptime(end_time, '%H:%M')
        end_time = end_time.replace(year=1900, month=1, day=1)
        
        # Initialize an empty list to store available movie names
        available_movie_names = []
        
        # Iterate over the movies
        for movie in self.movies:
            # Check if the movie is within the given time range
            if start_time <= movie['start_time'] < end_time or start_time < movie['end_time'] <= end_time:
                available_movie_names.append(movie['name'])
        
        return available_movie_names