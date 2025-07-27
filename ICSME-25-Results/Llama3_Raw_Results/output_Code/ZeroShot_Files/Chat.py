# This is a chat class with the functions of adding users, removing users, sending messages, and obtaining messages.

from datetime import datetime

class Chat:
    def __init__(self):
        # Initialize the Chat with an attribute users, which is an empty dictionary.
        self.users = {}
        # Initialize the messages attribute, which is an empty dictionary.
        self.messages = {}

    def add_user(self, username):
        # Add a new user to the Chat.
        # If the user is already in the Chat, returns False, otherwise, returns True.
        if username in self.users:
            return False
        else:
            self.users[username] = []
            self.messages[username] = []
            return True

    def remove_user(self, username):
        # Remove a user from the Chat.
        # If the user is already in the Chat, returns True, otherwise, returns False.
        if username in self.users:
            del self.users[username]
            del self.messages[username]
            # Remove messages sent to or from the removed user
            for user in self.messages:
                self.messages[user] = [message for message in self.messages[user] if message['sender'] != username and message['receiver'] != username]
            return True
        else:
            return False

    def send_message(self, sender, receiver, message):
        # Send a message from a user to another user.
        # If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        if sender in self.users and receiver in self.users:
            # Create a new message dictionary with the sender, receiver, message, and timestamp.
            new_message = {
                'sender': sender,
                'receiver': receiver,
                'message': message,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # Add the new message to the messages list of the receiver.
            self.messages[receiver].append(new_message)
            return True
        else:
            return False

    def get_messages(self, username):
        # Get all the messages of a user from the Chat.
        # Returns a list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        if username in self.messages:
            return self.messages[username]
        else:
            return []