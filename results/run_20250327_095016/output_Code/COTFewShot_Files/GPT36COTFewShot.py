from datetime import datetime

class EmailClient:
    def __init__(self, addr, capacity):
        self.addr = addr
        self.capacity = capacity
        self.inbox = []

    def send_to(self, recv, content, size):
        if recv.is_full_with_one_more_email(size):
            return False
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

    def fetch(self):
        for email in self.inbox:
            if email['state'] == 'unread':
                email['state'] = 'read'
                return email
        return None

    def is_full_with_one_more_email(self, size):
        return self.get_occupied_size() + size > self.capacity

    def get_occupied_size(self):
        return sum(email['size'] for email in self.inbox)

    def clear_inbox(self, size):
        while self.is_full_with_one_more_email(size):
            self.inbox.pop(0)