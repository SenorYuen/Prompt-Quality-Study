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
        new_datetime = self.datetime + datetime.timedelta(seconds=seconds)
        return new_datetime.strftime('%H:%M:%S')

    def string_to_datetime(self, string):
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

    def datetime_to_string(self, datetime):
        return datetime.strftime('%Y-%m-%d %H:%M:%S')

    def get_minutes(self, string_time1, string_time2):
        datetime1 = self.string_to_datetime(string_time1)
        datetime2 = self.string_to_datetime(string_time2)
        time_diff = datetime2 - datetime1
        minutes = round(time_diff.total_seconds() / 60)
        return minutes

    def get_format_time(self, year, month, day, hour, minute, second):
        return f'{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'