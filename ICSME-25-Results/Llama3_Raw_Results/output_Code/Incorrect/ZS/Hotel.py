class Hotel:
    def __init__(self, name, rooms):
        """
        Initialize the three fields in Hotel System.
        name is the hotel name.
        available_rooms stores the remaining rooms in the hotel
        booked_rooms stores the rooms that have been booked and the person's name who booked rooms.
        """
        self.name = name  # Hotel name
        self.available_rooms = rooms  # Dictionary with room types and quantities
        self.booked_rooms = {}  # Dictionary with room types and booking information

    def book_room(self, room_type, room_number, name):
        """
        Check if there are any rooms of the specified type available.
        if rooms are adequate, modify available_rooms and booked_rooms and finish booking, or fail to book otherwise.
        :return: if number of rooms about to be booked doesn't exceed the remaining rooms, return str 'Success!'
                if exceeds but quantity of available rooms is not equal to zero, return int(the remaining quantity of this room type).
                if exceeds and quantity is zero or the room_type isn't in available_room, return False.
        """
        # Check if room type is available
        if room_type not in self.available_rooms:
            return False
        
        # Check if there are enough rooms available
        if self.available_rooms[room_type] < room_number:
            # Return the remaining quantity of this room type
            if self.available_rooms[room_type] > 0:
                return self.available_rooms[room_type]
            else:
                return False
        
        # Update available rooms
        self.available_rooms[room_type] -= room_number
        
        # Update booked rooms
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        self.booked_rooms[room_type][name] = room_number
        
        return 'Success!'

    def check_in(self, room_type, room_number, name):
        """
        Check if the room of the specified type and number is booked by the person named name.
        Remove this name when check in successfuly(room_number is equal to specific person's booked_rooms. When the actual check in quantity (room_number) is less than the booked quantity, number in booked_rooms will be booked quantity minus actual quantity
        :return False: only if the room_type is not in the booked_rooms or room_number is higher than quantity in booked rooms.
        """
        # Check if room type is booked
        if room_type not in self.booked_rooms:
            return False
        
        # Check if person has booked rooms of this type
        if name not in self.booked_rooms[room_type]:
            return False
        
        # Check if the room number is valid
        if room_number > self.booked_rooms[room_type][name]:
            return False
        
        # Update booked rooms
        if room_number == self.booked_rooms[room_type][name]:
            del self.booked_rooms[room_type][name]
            if not self.booked_rooms[room_type]:
                del self.booked_rooms[room_type]
        else:
            self.booked_rooms[room_type][name] -= room_number
        
        return True

    def check_out(self, room_type, room_number):
        """
        Check out rooms, add number for specific type in available_rooms.
        If room_type is new, add new type in available_rooms.
        """
        # Add room number to available rooms
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        """
        Get the number of specific type of available rooms.
        :return: int, the remaining number of this type rooms.
        """
        # Return the number of available rooms of the specified type
        if room_type in self.available_rooms:
            return self.available_rooms[room_type]
        else:
            return 0