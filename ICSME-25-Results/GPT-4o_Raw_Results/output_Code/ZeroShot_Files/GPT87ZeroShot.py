import datetime
import time

class TimeUtils:

    def __init__(self):
        """
        Initialize the TimeUtils class and get the current datetime.
        """
        self.current_datetime = datetime.datetime.now()

    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'.
        :return: string
        """
        return self.current_datetime.strftime('%H:%M:%S')

    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d".
        :return: string
        """
        return self.current_datetime.strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time.
        :param seconds: number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        """
        new_time = self.current_datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance.
        :param string: time string in the format '%Y-%m-%d %H:%M:%S'
        :return: datetime instance
        """
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

    def datetime_to_string(self, dt):
        """
        Convert a datetime instance to a string.
        :param dt: datetime instance
        :return: string, converted time string in the format '%Y-%m-%d %H:%M:%S'
        """
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, string_time1, string_time2):
        """
        Calculate how many minutes have passed between two times, and round the results to the nearest minute.
        :param string_time1: first time string in the format '%Y-%m-%d %H:%M:%S'
        :param string_time2: second time string in the format '%Y-%m-%d %H:%M:%S'
        :return: int, the number of minutes between two times, rounded off
        """
        dt1 = self.string_to_datetime(string_time1)
        dt2 = self.string_to_datetime(string_time2)
        difference = dt2 - dt1
        return round(difference.total_seconds() / 60)

    def get_format_time(self, year, month, day, hour, minute, second):
        """
        Get formatted time from specified year, month, day, hour, minute, and second.
        :param year: int
        :param month: int
        :param day: int
        :param hour: int
        :param minute: int
        :param second: int
        :return: formatted time string in the format '%Y-%m-%d %H:%M:%S'
        """
        dt = datetime.datetime(year, month, day, hour, minute, second)
        return dt.strftime('%Y-%m-%d %H:%M:%S')