class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        if room_type not in self.available_rooms:
            return False
        if self.available_rooms[room_type] < room_number:
            return self.available_rooms[room_type]
        if self.available_rooms[room_type] == 0:
            return False
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        if name not in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][name] = 0
        self.booked_rooms[room_type][name] += room_number
        self.available_rooms[room_type] -= room_number
        return 'Success!'

    def check_in(self, room_type, room_number, name):
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            return False
        if self.booked_rooms[room_type][name] < room_number:
            return False
        if self.booked_rooms[room_type][name] == room_number:
            del self.booked_rooms[room_type][name]
            if len(self.booked_rooms[room_type]) == 0:
                del self.booked_rooms[room_type]
        else:
            self.booked_rooms[room_type][name] -= room_number
        return True

    def check_out(self, room_type, room_number):
        if room_type not in self.available_rooms:
            self.available_rooms[room_type] = 0
        self.available_rooms[room_type] += room_number

    def get_available_rooms(self, room_type):
        if room_type not in self.available_rooms:
            return 0
        return self.available_rooms[room_type]