import datetime
import time

class TimeUtils:

    # Initialize the class with the current datetime
    def __init__(self):
        self.current_datetime = datetime.datetime.now()

    # Return the current time in the format of '%H:%M:%S'
    def get_current_time(self):
        # Use strftime to format the current time
        return self.current_datetime.strftime('%H:%M:%S')

    # Return the current date in the format of "%Y-%m-%d"
    def get_current_date(self):
        # Use strftime to format the current date
        return self.current_datetime.strftime('%Y-%m-%d')

    # Add the specified number of seconds to the current time
    def add_seconds(self, seconds):
        # Calculate the new datetime by adding the specified number of seconds
        new_datetime = self.current_datetime + datetime.timedelta(seconds=seconds)
        # Use strftime to format the new time
        return new_datetime.strftime('%H:%M:%S')

    # Convert the time string to a datetime instance
    def string_to_datetime(self, string, format='%Y-%m-%d %H:%M:%S'):
        # Use strptime to parse the time string into a datetime instance
        return datetime.datetime.strptime(string, format)

    # Convert a datetime instance to a string
    def datetime_to_string(self, datetime, format='%Y-%m-%d %H:%M:%S'):
        # Use strftime to format the datetime instance into a string
        return datetime.strftime(format)

    # Calculate how many minutes have passed between two times, and round the results to the nearest
    def get_minutes(self, string_time1, string_time2):
        # Convert the time strings to datetime instances
        datetime1 = self.string_to_datetime(string_time1, format='%H:%M:%S')
        datetime2 = self.string_to_datetime(string_time2, format='%H:%M:%S')
        # Calculate the time difference
        time_diff = datetime2 - datetime1
        # Calculate the total seconds
        total_seconds = time_diff.total_seconds()
        # Convert the total seconds to minutes and round to the nearest minute
        minutes = round(total_seconds / 60)
        return minutes

    # get format time
    def get_format_time(self, year, month, day, hour, minute, second):
        # Create a new datetime instance with the specified time
        datetime = datetime.datetime(year, month, day, hour, minute, second)
        # Use strftime to format the datetime instance into a string
        return datetime.strftime('%Y-%m-%d %H:%M:%S')