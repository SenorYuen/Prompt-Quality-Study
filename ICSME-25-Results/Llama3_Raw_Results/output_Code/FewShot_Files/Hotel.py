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
        Check if there are any rooms of the specified type available.
        if rooms are adequate, modify available_rooms and booked_rooms and finish booking, or fail to book otherwise.
        :param room_type: str
        :param room_number: int, the expected number of specified type rooms to be booked
        :param name: str, guest name
        :return: if number of rooms about to be booked doesn't exceed the remaining rooms, return str 'Success!'
                if exceeds but quantity of available rooms is not equal to zero, return int(the remaining quantity of this room type).
                if exceeds and quantity is zero or the room_type isn't in available_room, return False.
        """
        # Check if room type exists in available rooms
        if room_type not in self.available_rooms:
            return False
        
        # Check if the number of rooms to book exceeds the available rooms
        if room_number > self.available_rooms[room_type]:
            # If exceeds but available rooms are not zero, return the remaining quantity
            if self.available_rooms[room_type] != 0:
                return self.available_rooms[room_type]
            # If exceeds and available rooms are zero, return False
            else:
                return False
        
        # If rooms are adequate, modify available_rooms and booked_rooms
        self.available_rooms[room_type] -= room_number
        
        # Initialize booked_rooms for the room type if it doesn't exist
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        
        # Add the guest to the booked rooms
        if name in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][name] += room_number
        else:
            self.booked_rooms[room_type][name] = room_number
        
        return 'Success!'

    def check_in(self, room_type, room_number, name):
        """
        Check if the room of the specified type and number is booked by the person named name.
        Remove this name when check in successfuly(room_number is equal to specific person's booked_rooms. When the actual check in quantity (room_number) is less than the booked quantity, number in booked_rooms will be booked quantity minus actual quantity
        :param room_type: str, check in room type
        :param room_number: int, check in room number
        :param name: str, person name
        :return False: only if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
        """
        # Check if room type exists in booked rooms
        if room_type not in self.booked_rooms:
            return False
        
        # Check if the guest has booked rooms of the specified type
        if name not in self.booked_rooms[room_type]:
            return False
        
        # Check if the number of rooms to check in exceeds the booked rooms
        if room_number > self.booked_rooms[room_type][name]:
            return False
        
        # Update the booked rooms
        self.booked_rooms[room_type][name] -= room_number
        
        # Remove the guest from the booked rooms if all rooms have been checked in
        if self.booked_rooms[room_type][name] == 0:
            del self.booked_rooms[room_type][name]
        
        # Remove the room type from the booked rooms if no guests have booked rooms of this type
        if len(self.booked_rooms[room_type]) == 0:
            del self.booked_rooms[room_type]

    def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        :param room_type: str, check out room type
        :param room_number: int, check out room number
        """
        # Add the checked out rooms to the available rooms
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :param room_type: str, the room type that want to know
        :return: int, the remaining number of this type rooms.
        """
        # Return the number of available rooms of the specified type
        if room_type in self.available_rooms:
            return self.available_rooms[room_type]
        else:
            return 0