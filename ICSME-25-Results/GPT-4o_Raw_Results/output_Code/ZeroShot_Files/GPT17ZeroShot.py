from datetime import datetime, timedelta

class CalendarUtil:
    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: A dictionary with 'start' and 'end' datetime objects.
        """
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: A dictionary with 'start' and 'end' datetime objects.
        """
        self.events.remove(event)

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: A datetime.date object.
        :return: A list of events on the given date.
        """
        return [event for event in self.events if event['start'].date() == date]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: A datetime object for the start of the time slot.
        :param end_time: A datetime object for the end of the time slot.
        :return: True if the calendar is available for the given time slot, False otherwise.
        """
        for event in self.events:
            if not (end_time <= event['start'] or start_time >= event['end']):
                return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: A datetime.date object.
        :return: A list of available time slots on the given date.
        """
        events_on_date = self.get_events(date)
        events_on_date.sort(key=lambda x: x['start'])

        available_slots = []
        start_of_day = datetime.combine(date, datetime.min.time())
        end_of_day = datetime.combine(date, datetime.max.time())

        current_time = start_of_day

        for event in events_on_date:
            if current_time < event['start']:
                available_slots.append({'start': current_time, 'end': event['start']})
            current_time = max(current_time, event['end'])

        if current_time < end_of_day:
            available_slots.append({'start': current_time, 'end': end_of_day})

        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from the current date and time.
        :param num_events: Number of upcoming events to retrieve.
        :return: A list of the next n upcoming events.
        """
        now = datetime.now()
        future_events = [event for event in self.events if event['start'] >= now]
        future_events.sort(key=lambda x: x['start'])
        return future_events[:num_events]