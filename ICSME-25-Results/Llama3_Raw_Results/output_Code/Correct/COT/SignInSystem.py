class SignInSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = False
            return True
        return False

    def sign_in(self, username):
        if username in self.users:
            self.users[username] = True
            return True
        return False

    def check_sign_in(self, username):
        if username in self.users and self.users[username]:
            return True
        return False

    def all_signed_in(self):
        return all(status for status in self.users.values())

    def all_not_signed_in(self):
        return [username for username, status in self.users.items() if not status]