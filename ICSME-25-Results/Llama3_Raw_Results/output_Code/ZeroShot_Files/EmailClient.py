from datetime import datetime

class EmailClient:
    def __init__(self, addr, capacity) -> None:
        # Initialize the email address and capacity of the email box
        self.addr = addr
        self.capacity = capacity
        # Initialize an empty list to store emails
        self.emails = []
        # Initialize the total occupied size to 0
        self.occupied_size = 0.0

    def send_to(self, recv, content, size):
        # Check if the receiver's email box has enough space
        if self.is_full_with_one_more_email(size):
            return False
        # Create a new email with the given content and size
        email = {
            "sender": self.addr,
            "receiver": recv,
            "content": content,
            "size": size,
            "timestamp": datetime.now(),
            "read": False
        }
        # Add the email to the email box
        self.emails.append(email)
        # Update the occupied size
        self.occupied_size += size
        return True

    def fetch(self):
        # Find the first unread email in the email box
        for email in self.emails:
            if not email["read"]:
                # Mark the email as read
                email["read"] = True
                return email
        # If no unread emails are found, return None
        return None

    def is_full_with_one_more_email(self, size):
        # Check if the email box is full after adding an email of the given size
        return self.occupied_size + size > self.capacity

    def get_occupied_size(self):
        # Return the total occupied size of the email box
        return self.occupied_size

    def clear_inbox(self, size):
        # Sort the emails by timestamp
        self.emails.sort(key=lambda x: x["timestamp"])
        # Delete the oldest emails until the email box has enough space
        while self.occupied_size + size > self.capacity and self.emails:
            email = self.emails.pop(0)
            self.occupied_size -= email["size"]