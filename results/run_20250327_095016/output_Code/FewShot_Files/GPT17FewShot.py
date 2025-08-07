from datetime import datetime, timedelta

class CalendarUtil:
    """
    This is a class as CalendarUtil that provides functionalities to manage calendar events, schedule appointments, and perform conflict checks.
    """

    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.
        :param event: The event to be added to the calendar, dict.
        """
        # Append the event to the list of events
        self.events.append(event)

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        :param event: The event to be removed from the calendar, dict.
        """
        # Remove the event from the list of events if it exists
        if event in self.events:
            self.events.remove(event)

    def get_events(self, date):
        """
        Get all events on a given date.
        :param date: The date to get events for, datetime.
        :return: A list of events on the given date, list.
        """
        # Filter events that match the given date and return them
        return [event for event in self.events if event['date'].date() == date.date()]

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :param start_time: The start time of the time slot, datetime.
        :param end_time: The end time of the time slot, datetime.
        :return: True if the calendar is available for the given time slot, False otherwise, bool.
        """
        # Check if any existing event overlaps with the given time slot
        for event in self.events:
            if event['start_time'] < end_time and event['end_time'] > start_time:
                return False
        return True

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :param date: The date to get available time slots for, datetime.
        :return: A list of available time slots on the given date, list.
        """
        # Define the start and end of the day
        start_of_day = datetime(date.year, date.month, date.day)
        end_of_day = start_of_day + timedelta(days=1)

        # Sort events by start time
        events_on_date = sorted(self.get_events(date), key=lambda x: x['start_time'])

        # Initialize available slots list
        available_slots = []

        # Track the end of the last event
        last_end_time = start_of_day

        # Find gaps between events
        for event in events_on_date:
            if last_end_time < event['start_time']:
                available_slots.append((last_end_time, event['start_time']))
            last_end_time = max(last_end_time, event['end_time'])

        # Check for available slot after the last event
        if last_end_time < end_of_day:
            available_slots.append((last_end_time, end_of_day))

        return available_slots

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from the current date.
        :param num_events: The number of upcoming events to get, int.
        :return: A list of the next n upcoming events, list.
        """
        # Sort events by start time
        sorted_events = sorted(self.events, key=lambda x: x['start_time'])

        # Return the next n events
        return sorted_events[:num_events]