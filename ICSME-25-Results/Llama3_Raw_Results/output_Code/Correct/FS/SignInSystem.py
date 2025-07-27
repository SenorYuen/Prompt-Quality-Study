class SignInSystem:
    """
    This is a class as sign-in system, including adding users, signing in/out, checking sign-in status, and retrieving signed-in/not signed-in users.
    """

    def __init__(self):
        """
        Initialize the sign-in system.
        """
        # Initialize an empty dictionary to store users and their sign-in status
        self.users = {}

    def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        And the initial state is False.
        :param username: str, the username to be added.
        :return: bool, True if the user is added successfully, False if the user already exists.
        """
        # Check if the user already exists in the system
        if username not in self.users:
            # Add the user with an initial sign-in status of False
            self.users[username] = False
            return True
        else:
            # Return False if the user already exists
            return False

    def sign_in(self, username):
        """
        Sign in a user if the user was in the self.users and change the state to True.
        :param username: str, the username to be signed in.
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        """
        # Check if the user exists in the system
        if username in self.users:
            # Sign in the user by setting their status to True
            self.users[username] = True
            return True
        else:
            # Return False if the user does not exist
            return False

    def check_sign_in(self, username):
        """
        Check if a user is signed in.
        :param username: str, the username to be checked.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        """
        # Check if the user exists in the system
        if username in self.users:
            # Return the sign-in status of the user
            return self.users[username]
        else:
            # Return False if the user does not exist
            return False

    def all_signed_in(self):
        """
        Check if all users are signed in.
        :return: bool, True if all users are signed in, False otherwise.
        """
        # Iterate over all users in the system
        for user in self.users:
            # If any user is not signed in, return False
            if not self.users[user]:
                return False
        # If all users are signed in, return True
        return True

    def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        :return: list[str], a list of usernames that are not signed in.
        """
        # Initialize an empty list to store usernames of users who are not signed in
        not_signed_in_users = []
        # Iterate over all users in the system
        for user in self.users:
            # If a user is not signed in, add them to the list
            if not self.users[user]:
                not_signed_in_users.append(user)
        # Return the list of usernames of users who are not signed in
        return not_signed_in_users