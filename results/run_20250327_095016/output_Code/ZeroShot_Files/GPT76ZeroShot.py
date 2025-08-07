class SignInSystem:
    def __init__(self):
        """
        Initialize the sign-in system with an empty dictionary to hold users and their sign-in status.
        """
        self.users = {}

    def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        The initial state is False (not signed in).
        
        :param username: str, the username to add
        :return: bool, True if the user is added successfully, False if the user already exists.
        """
        if username not in self.users:
            self.users[username] = False  # Set initial sign-in status to False
            return True
        return False

    def sign_in(self, username):
        """
        Sign in a user if the user exists in the self.users and change the state to True.
        
        :param username: str, the username to sign in
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        """
        if username in self.users:
            self.users[username] = True  # Change sign-in status to True
            return True
        return False

    def check_sign_in(self, username):
        """
        Check if a user is signed in.
        
        :param username: str, the username to check
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        """
        return self.users.get(username, False)

    def all_signed_in(self):
        """
        Check if all users are signed in.
        
        :return: bool, True if all users are signed in, False otherwise.
        """
        return all(self.users.values())

    def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        
        :return: list[str], a list of usernames that are not signed in.
        """
        return [username for username, signed_in in self.users.items() if not signed_in]