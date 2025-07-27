from datetime import datetime, timedelta

class CalendarUtil:
    def __init__(self):
        # Initialize the calendar with an empty list of events
        self.events = []

    def add_event(self, event):
        # Add an event to the calendar
        # Event should be a dictionary with 'start_time', 'end_time', and 'date' keys
        self.events.append(event)

    def remove_event(self, event):
        # Remove an event from the calendar
        # Event should be a dictionary with 'start_time', 'end_time', and 'date' keys
        self.events = [e for e in self.events if e != event]

    def get_events(self, date):
        # Get all events on a given date
        # Date should be a datetime object
        return [event for event in self.events if event['date'] == date.date()]

    def is_available(self, start_time, end_time):
        # Check if the calendar is available for a given time slot
        # Start_time and end_time should be datetime objects
        for event in self.events:
            if (start_time >= event['start_time'] and start_time < event['end_time']) or \
               (end_time > event['start_time'] and end_time <= event['end_time']) or \
               (start_time <= event['start_time'] and end_time >= event['end_time']):
                return False
        return True

    def get_available_slots(self, date):
        # Get all available time slots on a given date
        # Date should be a datetime object
        available_slots = []
        start_time = datetime.combine(date, datetime.min.time())
        end_time = datetime.combine(date, datetime.min.time()) + timedelta(minutes=30)
        while end_time <= datetime.combine(date, datetime.max.time()):
            if self.is_available(start_time, end_time):
                available_slots.append((start_time, end_time))
            start_time += timedelta(minutes=30)
            end_time += timedelta(minutes=30)
        return available_slots

    def get_upcoming_events(self, num_events):
        # Get the next n upcoming events from a given date
        # Date should be a datetime object
        upcoming_events = sorted(self.events, key=lambda x: x['start_time'])
        return upcoming_events[:num_events]

# Example usage:
calendar = CalendarUtil()
event1 = {'start_time': datetime(2024, 9, 16, 10), 'end_time': datetime(2024, 9, 16, 11), 'date': datetime(2024, 9, 16).date()}
event2 = {'start_time': datetime(2024, 9, 16, 12), 'end_time': datetime(2024, 9, 16, 13), 'date': datetime(2024, 9, 16).date()}
calendar.add_event(event1)
calendar.add_event(event2)
print(calendar.get_events(datetime(2024, 9, 16).date()))
print(calendar.is_available(datetime(2024, 9, 16, 11), datetime(2024, 9, 16, 12)))
print(calendar.get_available_slots(datetime(2024, 9, 16).date()))
print(calendar.get_upcoming_events(2))