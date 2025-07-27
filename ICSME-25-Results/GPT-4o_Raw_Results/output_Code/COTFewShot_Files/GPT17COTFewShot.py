from datetime import datetime, timedelta

class CalendarUtil:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self, date):
        return [event for event in self.events if event['date'].date() == date.date()]

    def remove_event(self, event):
        self.events.remove(event)

    def is_available(self, start_time, end_time):
        for event in self.events:
            if event['start_time'] < end_time and event['end_time'] > start_time:
                return False
        return True

    def get_available_slots(self, date):
        slots = []
        start_of_day = datetime(date.year, date.month, date.day)
        end_of_day = start_of_day + timedelta(days=1)
        current_time = start_of_day

        for event in sorted(self.get_events(date), key=lambda e: e['start_time']):
            if current_time < event['start_time']:
                slots.append((current_time, event['start_time']))
            current_time = max(current_time, event['end_time'])

        if current_time < end_of_day:
            slots.append((current_time, end_of_day))

        return slots

    def get_upcoming_events(self, num_events):
        sorted_events = sorted(self.events, key=lambda e: e['start_time'])
        return sorted_events[:num_events]