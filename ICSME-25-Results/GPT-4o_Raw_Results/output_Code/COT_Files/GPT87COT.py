import datetime
import time

class TimeUtils:
    def __init__(self):
        self.datetime = datetime.datetime.now()

    def get_current_time(self):
        return self.datetime.strftime('%H:%M:%S')

    def get_current_date(self):
        return self.datetime.strftime('%Y-%m-%d')

    def add_seconds(self, seconds):
        new_time = self.datetime + datetime.timedelta(seconds=seconds)
        return new_time.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

    def datetime_to_string(self, datetime_obj):
        return datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, string_time1, string_time2):
        dt1 = self.string_to_datetime(string_time1)
        dt2 = self.string_to_datetime(string_time2)
        delta = dt2 - dt1
        return round(delta.total_seconds() / 60)

    def get_format_time(self, year, month, day, hour, minute, second):
        formatted_time = datetime.datetime(year, month, day, hour, minute, second)
        return formatted_time.strftime('%Y-%m-%d %H:%M:%S')