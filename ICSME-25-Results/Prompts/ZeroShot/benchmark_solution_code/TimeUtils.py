'''
# This is a time util class, including getting the current time and date, adding seconds to a datetime, converting between strings and datetime objects, calculating the time difference in minutes, and formatting a datetime object.

import datetime
import time

class TimeUtils:

    def __init__(self):
        """
        Get the current datetime
        """

    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        """

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        """

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :return: datetime instance
        """

    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :return: string, converted time string
        """

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        """

    def get_format_time(self, year, month, day, hour, minute, second):
        """
        get format time
        :return: formatted time string
        """
'''

import datetime
import time

class TimeUtils:

    def __init__(self):
        self.datetime = datetime.datetime.now()

    def get_current_time(self):
        format = "%H:%M:%S"
        return self.datetime.strftime(format)

    def get_current_date(self):
        format = "%Y-%m-%d"
        return self.datetime.strftime(format)

    def add_seconds(self, seconds):
        new_datetime = self.datetime + datetime.timedelta(seconds=seconds)
        format = "%H:%M:%S"
        return new_datetime.strftime(format)

    def string_to_datetime(self, string):
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

    def datetime_to_string(self, datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")

    def get_minutes(self, string_time1, string_time2):
        time1 = self.string_to_datetime(string_time1)
        time2 = self.string_to_datetime(string_time2)
        return round((time2 - time1).seconds / 60)

    def get_format_time(self, year, month, day, hour, minute, second):
        format = "%Y-%m-%d %H:%M:%S"
        time_item = datetime.datetime(year, month, day, hour, minute, second)
        return time_item.strftime(format)




