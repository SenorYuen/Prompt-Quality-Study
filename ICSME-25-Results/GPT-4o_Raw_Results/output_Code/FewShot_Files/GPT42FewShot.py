class Hotel:
    """
    This is a class as hotel management system, managing the booking, check-in, check-out, and availability of rooms in a hotel with different room types.
    """

    def __init__(self, name, rooms):
        """
        Initialize the three fields in Hotel System.
        name is the hotel name.
        available_rooms stores the remaining rooms in the hotel
        booked_rooms stores the rooms that have been booked and the person's name who booked rooms.
        """
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        """
        Book rooms of a specified type if available.
        """
        if room_type not in self.available_rooms or self.available_rooms[room_type] == 0:
            return False
        if room_number > self.available_rooms[room_type]:
            return self.available_rooms[room_type]
        
        # Deduct the booked rooms from available rooms
        self.available_rooms[room_type] -= room_number
        
        # Add to booked rooms
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        
        if name in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][name] += room_number
        else:
            self.booked_rooms[room_type][name] = room_number
        
        return 'Success!'

    def check_in(self, room_type, room_number, name):
        """
        Check in the booked rooms for the specified guest.
        """
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            return False
        if room_number > self.booked_rooms[room_type][name]:
            return False
        
        # Reduce the booked room count
        self.booked_rooms[room_type][name] -= room_number
        if self.booked_rooms[room_type][name] == 0:
            del self.booked_rooms[room_type][name]
        
        return True

    def check_out(self, room_type, room_number):
        """
        Check out rooms and update available rooms.
        """
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        """
        return self.available_rooms.get(room_type, 0)