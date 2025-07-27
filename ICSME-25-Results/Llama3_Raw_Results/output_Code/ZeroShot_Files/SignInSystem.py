class SignInSystem:
    def __init__(self):
        # Initialize an empty dictionary to store users and their sign-in status
        self.users = {}

    def add_user(self, username):
        # Check if the user already exists in the system
        if username not in self.users:
            # Add the user with initial sign-in status as False
            self.users[username] = False
            return True  # Return True if the user is added successfully
        return False  # Return False if the user already exists

    def sign_in(self, username):
        # Check if the user exists in the system
        if username in self.users:
            # Sign in the user by changing their status to True
            self.users[username] = True
            return True  # Return True if the user is signed in successfully
        return False  # Return False if the user does not exist

    def check_sign_in(self, username):
        # Check if the user exists in the system and is signed in
        return username in self.users and self.users[username]

    def all_signed_in(self):
        # Check if all users are signed in by verifying that all values in the dictionary are True
        return all(self.users.values())

    def all_not_signed_in(self):
        # Get a list of usernames that are not signed in by filtering the dictionary
        return [username for username, signed_in in self.users.items() if not signed_in]