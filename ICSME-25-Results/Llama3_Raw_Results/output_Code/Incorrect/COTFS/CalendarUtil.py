from datetime import datetime, timedelta

class CalendarUtil:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self, date):
        return [event for event in self.events if event['date'].date() == date.date()]

    def remove_event(self, event):
        self.events = [e for e in self.events if e != event]

    def is_available(self, start_time, end_time):
        for event in self.events:
            if (start_time >= event['start_time'] and start_time < event['end_time']) or (end_time > event['start_time'] and end_time <= event['end_time']) or (start_time <= event['start_time'] and end_time >= event['end_time']):
                return False
        return True

    def get_available_slots(self, date):
        available_slots = []
        start_time = datetime.combine(date, datetime.min.time())
        end_time = datetime.combine(date, datetime.max.time())
        for event in sorted(self.events, key=lambda x: x['start_time']):
            if event['date'].date() == date.date():
                if start_time < event['start_time']:
                    available_slots.append((start_time, event['start_time']))
                start_time = event['end_time']
        if start_time < end_time:
            available_slots.append((start_time, end_time))
        return available_slots

    def get_upcoming_events(self, num_events):
        upcoming_events = sorted(self.events, key=lambda x: x['start_time'])
        return upcoming_events[:num_events]