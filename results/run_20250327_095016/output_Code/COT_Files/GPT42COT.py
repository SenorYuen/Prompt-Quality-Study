class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.available_rooms = rooms
        self.booked_rooms = {}

    def book_room(self, room_type, room_number, name):
        if room_type not in self.available_rooms or self.available_rooms[room_type] == 0:
            return False
        if room_number > self.available_rooms[room_type]:
            return self.available_rooms[room_type]
        self.available_rooms[room_type] -= room_number
        if room_type not in self.booked_rooms:
            self.booked_rooms[room_type] = {}
        if name in self.booked_rooms[room_type]:
            self.booked_rooms[room_type][name] += room_number
        else:
            self.booked_rooms[room_type][name] = room_number
        return 'Success!'

    def check_in(self, room_type, room_number, name):
        if room_type not in self.booked_rooms or name not in self.booked_rooms[room_type]:
            return False
        if room_number > self.booked_rooms[room_type][name]:
            return False
        self.booked_rooms[room_type][name] -= room_number
        if self.booked_rooms[room_type][name] == 0:
            del self.booked_rooms[room_type][name]
        if not self.booked_rooms[room_type]:
            del self.booked_rooms[room_type]
        return True

    def check_out(self, room_type, room_number):
        if room_type in self.available_rooms:
            self.available_rooms[room_type] += room_number
        else:
            self.available_rooms[room_type] = room_number

    def get_available_rooms(self, room_type):
        return self.available_rooms.get(room_type, 0)