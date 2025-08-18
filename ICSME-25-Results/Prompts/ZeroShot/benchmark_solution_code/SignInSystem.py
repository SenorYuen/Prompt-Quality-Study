'''
# This is a class as sigin in system, including adding users, signing in/out, checking sign-in status, and retrieving signed-in/not signed-in users.

class SignInSystem:
    def __init__(self):
        """
        Initialize the sign-in system.
        """

    def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        And the initial state is False.
        :return: bool, True if the user is added successfully, False if the user already exists.
        """

    def sign_in(self, username):
        """
        Sign in a user if the user was in the self.users and change the state to True.
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        """

    def check_sign_in(self, username):
        """
        Check if a user is signed in.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        """

    def all_signed_in(self):
        """
        Check if all users are signed in.
        :return: bool, True if all users are signed in, False otherwise.
        """

    def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        :return: list[str], a list of usernames that are not signed in.
        """
'''


class SignInSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username in self.users:
            return False
        else:
            self.users[username] = False
            return True

    def sign_in(self, username):
        if username not in self.users:
            return False
        else:
            self.users[username] = True
            return True

    def check_sign_in(self, username):
        if username not in self.users:
            return False
        else:
            if self.users[username]:
                return True
            else:
                return False

    def all_signed_in(self):
        if all(self.users.values()):
            return True
        else:
            return False

    def all_not_signed_in(self):
        not_signed_in_users = []
        for username, signed_in in self.users.items():
            if not signed_in:
                not_signed_in_users.append(username)
        return not_signed_in_users
