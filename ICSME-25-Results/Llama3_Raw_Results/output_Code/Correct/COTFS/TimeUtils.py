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
        datetime1 = datetime.datetime.strptime(string_time1, '%Y-%m-%d %H:%M:%S')
        datetime2 = datetime.datetime.strptime(string_time2, '%Y-%m-%d %H:%M:%S')
        time_diff = abs((datetime2 - datetime1).total_seconds() / 60)
        return round(time_diff)

    def get_format_time(self, year, month, day, hour, minute, second):
        return f'{year:04}-{month:02}-{day:02} {hour:02}:{minute:02}:{second:02}'