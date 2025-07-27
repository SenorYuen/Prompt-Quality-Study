class Chat:
    """
    This is a chat class with the functions of adding users, removing users, sending messages, and obtaining messages.
    """

    def __init__(self):
        """
        Initialize the Chat with an attribute users, which is an empty dictionary.
        """
        # Initialize an empty dictionary to store users and their messages
        self.users = {}

    def add_user(self, username):
        """
        Add a new user to the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns False, otherwise, returns True.
        """
        # Check if the user already exists in the chat
        if username in self.users:
            # If the user exists, return False
            return False
        else:
            # If the user does not exist, add them to the chat with an empty list of messages
            self.users[username] = []
            # Return True to indicate that the user was added successfully
            return True

    def remove_user(self, username):
        """
        Remove a user from the Chat.
        :param username: The user's name, str.
        :return: If the user is already in the Chat, returns True, otherwise, returns False.
        """
        # Check if the user exists in the chat
        if username in self.users:
            # If the user exists, remove them from the chat
            del self.users[username]
            # Return True to indicate that the user was removed successfully
            return True
        else:
            # If the user does not exist, return False
            return False

    def send_message(self, sender, receiver, message):
        """
        Send a message from a user to another user.
        :param sender: The sender's name, str.
        :param receiver: The receiver's name, str.
        :param message: The message, str.
        :return: If the sender or the receiver is not in the Chat, returns False, otherwise, returns True.
        """
        # Check if both the sender and receiver exist in the chat
        if sender in self.users and receiver in self.users:
            # If both users exist, create a new message with the current timestamp
            new_message = {
                'sender': sender,
                'receiver': receiver,
                'message': message,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # Add the new message to the receiver's list of messages
            self.users[receiver].append(new_message)
            # Return True to indicate that the message was sent successfully
            return True
        else:
            # If either the sender or receiver does not exist, return False
            return False

    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        """
        # Check if the user exists in the chat
        if username in self.users:
            # If the user exists, return their list of messages
            return self.users[username]
        else:
            # If the user does not exist, return an empty list
            return []