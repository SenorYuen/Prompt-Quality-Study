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
        return self.users.get(username, False)

    def all_signed_in(self):
        return all(self.users.values())

    def all_not_signed_in(self):
        return [username for username, signed_in in self.users.items() if not signed_in]