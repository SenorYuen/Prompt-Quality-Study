from datetime import datetime

class Chat:
    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        The dictionary will store usernames as keys and a list of messages as values.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the Chat.
        :param username: The username of the user to add.
        :return: If the user is already in the Chat, returns False, otherwise, returns True.
        """
        if username in self.users:
            return False
        else:
            self.users[username] = []  # Initialize the user's message list
            return True

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The username of the user to remove.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
        """
        if username in self.users:
            del self.users[username]  # Remove the user from the dictionary
            return True
        else:
            return False

    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The username of the sender.
        :param receiver: The username of the receiver.
        :param message: The content of the message.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        """
        if sender not in self.users or receiver not in self.users:
            return False
        else:
            # Create a message dictionary with sender, receiver, message, and timestamp
            msg = {
                'sender': sender,
                'receiver': receiver,
                'message': message,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # Append the message to the sender's message list
            self.users[sender].append(msg)
            # Append the message to the receiver's message list
            self.users[receiver].append(msg)
            return True

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The username of the user whose messages are to be retrieved.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        """
        if username in self.users:
            return self.users[username]  # Return the list of messages for the user
        else:
            return []  # Return an empty list if the user is not found