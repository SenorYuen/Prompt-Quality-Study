from datetime import datetime

class EmailClient:
    def __init__(self, addr, capacity) -> None:
        """
        Initializes the EmailClient class with the email address and the capacity of the email box.
        :param addr: The email address of the client, str.
        :param capacity: The total capacity of the email box, float.
        """
        self.address = addr
        self.capacity = capacity
        self.inbox = []  # List to store emails as dictionaries
        self.occupied_size = 0.0  # To track the current size used in the inbox

    def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The receiver's email address, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        """
        if recv.is_full_with_one_more_email(size):
            return False
        recv.inbox.append({
            'sender': self.address,
            'content': content,
            'size': size,
            'read': False,
            'timestamp': datetime.now()
        })
        recv.occupied_size += size
        return True

    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        """
        for email in self.inbox:
            if not email['read']:
                email['read'] = True
                return email
        return None  # Return None if no unread email is found

    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the incoming email, float.
        :return: True if the email box is full, False otherwise.
        """
        return self.occupied_size + size > self.capacity

    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        return self.occupied_size

    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email to accommodate, float.
        """
        # Sort emails by timestamp to remove the oldest first
        self.inbox.sort(key=lambda email: email['timestamp'])
        while self.is_full_with_one_more_email(size):
            if self.inbox:
                oldest_email = self.inbox.pop(0)
                self.occupied_size -= oldest_email['size']
            else:
                break  # Break if there are no emails left to delete