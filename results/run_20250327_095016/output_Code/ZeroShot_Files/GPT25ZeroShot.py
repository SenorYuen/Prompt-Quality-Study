import json

class CookiesUtil:
    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The file path where cookies will be stored.
        """
        self.cookies_file = cookies_file
        self.cookies_data = {}

    def get_cookies(self, response):
        """
        Gets the cookies from the specified response and saves them to cookies_file.
        :param response: The response object from which to extract cookies.
        """
        # Extract cookies from the response
        self.cookies_data = response.cookies.get_dict()
        # Save cookies to file
        self._save_cookies()

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        try:
            with open(self.cookies_file, 'r') as file:
                self.cookies_data = json.load(file)
        except FileNotFoundError:
            # If the file does not exist, return an empty dictionary
            self.cookies_data = {}
        except json.JSONDecodeError:
            # If the file is not a valid JSON, return an empty dictionary
            self.cookies_data = {}
        return self.cookies_data

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        try:
            with open(self.cookies_file, 'w') as file:
                json.dump(self.cookies_data, file)
            return True
        except IOError:
            # If there is an IOError, return False
            return False