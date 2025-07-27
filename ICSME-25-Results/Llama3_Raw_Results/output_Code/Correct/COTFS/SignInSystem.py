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
        for user in self.users.values():
            if not user:
                return False
        return True

    def all_not_signed_in(self):
        return [username for username, signed_in in self.users.items() if not signed_in]