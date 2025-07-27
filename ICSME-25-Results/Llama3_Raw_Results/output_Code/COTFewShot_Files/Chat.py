from datetime import datetime


class Chat:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username in self.users:
            return False
        else:
            self.users[username] = []
            return True

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        else:
            return False

    def send_message(self, sender, receiver, message):
        if sender not in self.users or receiver not in self.users:
            return False
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.users[sender].append({
                'sender': sender,
                'receiver': receiver,
                'message': message,
                'timestamp': timestamp
            })
            self.users[receiver].append({
                'sender': sender,
                'receiver': receiver,
                'message': message,
                'timestamp': timestamp
            })
            return True

    def get_messages(self, username):
        if username in self.users:
            return self.users[username]
        else:
            return []