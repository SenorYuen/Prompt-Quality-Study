from datetime import datetime

class EmailClient:
    """
    This is a class that serves as an email client, implementing functions such as checking emails, determining whether there is sufficient space, and cleaning up space
    """

    def __init__(self, addr, capacity) -> None:
        """
        Initializes the EmailClient class with the email address and the capacity of the email box.
        :param addr: The email address, str.
        :param capacity: The capacity of the email box, float.
        """
        self.addr = addr
        self.capacity = capacity
        self.inbox = []

    # Method to send an email to the given email address
    def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        """
        # Check if the receiver's email box has enough space
        if recv.is_full_with_one_more_email(size):
            return False
        
        # Create a new email and add it to the receiver's inbox
        email = {
            'sender': self.addr,
            'receiver': recv.addr,
            'content': content,
            'size': size,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'state': 'unread'
        }
        recv.inbox.append(email)
        return True

    # Method to retrieve the first unread email in the email box and mark it as read
    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        """
        # Find the first unread email in the inbox
        for email in self.inbox:
            if email['state'] == 'unread':
                # Mark the email as read
                email['state'] = 'read'
                return email
        return None

    # Method to determine whether the email box is full after adding an email of the given size
    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        """
        # Calculate the total size of the emails in the inbox
        total_size = self.get_occupied_size()
        # Check if adding the new email would exceed the capacity
        return total_size + size > self.capacity

    # Method to get the total size of the emails in the email box
    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        # Calculate the total size of the emails in the inbox
        total_size = sum(email['size'] for email in self.inbox)
        return total_size

    # Method to clear the email box by deleting the oldest emails until the email box has enough space to accommodate the given size
    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        # Calculate the total size of the emails in the inbox
        total_size = self.get_occupied_size()
        # Delete the oldest emails until there is enough space
        while total_size + size > self.capacity:
            # Remove the oldest email from the inbox
            oldest_email = self.inbox.pop(0)
            # Update the total size
            total_size -= oldest_email['size']