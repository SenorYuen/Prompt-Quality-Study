'''
# This is a chat class with the functions of adding users, removing users, sending messages, and obtaining messages.

from datetime import datetime

class Chat:
    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """

    def add_user(self, username):
        """
        Add a new user to the Chat.
        :return: If the user is already in the Chat, returns False, otherwise, returns True.
        """

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
        """

    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        """

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        """
'''

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

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_info = {
            'sender': sender,
            'receiver': receiver,
            'message': message,
            'timestamp': timestamp
        }
        self.users[sender].append(message_info)
        self.users[receiver].append(message_info)
        return True

    def get_messages(self, username):
        if username not in self.users:
            return []
        return self.users[username]