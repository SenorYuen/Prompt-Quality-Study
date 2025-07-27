from datetime import datetime
import numpy as np

class MovieBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, price, start_time, end_time, n):
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        seats = np.zeros((n, n))
        movie = {
            'name': name,
            'price': price,
            'start_time': start_time,
            'end_time': end_time,
            'seats': seats
        }
        self.movies.append(movie)

    def book_ticket(self, name, seats_to_book):
        for movie in self.movies:
            if movie['name'].lower() == name.lower():
                for seat in seats_to_book:
                    if movie['seats'][seat] == 1:
                        return "Booking failed."
                for seat in seats_to_book:
                    movie['seats'][seat] = 1
                return "Booking success."
        return "Movie not found."

    def available_movies(self, start_time, end_time):
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        available = []
        for movie in self.movies:
            if movie['start_time'] >= start_time and movie['end_time'] <= end_time:
                available.append(movie['name'])
        return available