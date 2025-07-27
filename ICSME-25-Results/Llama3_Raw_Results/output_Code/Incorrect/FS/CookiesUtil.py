import json

class CookiesUtil:
    """
    This is a class as utility for managing and manipulating Cookies, including methods for retrieving, saving, and setting Cookies data.
    """

    def __init__(self, cookies_file):
        """
        Initializes the CookiesUtil with the specified cookies file.
        :param cookies_file: The cookies file to use, str.
        """
        self.cookies_file = cookies_file
        self.cookies = None

    def get_cookies(self, response):
        """
        Gets the cookies from the specified response, and save it to cookies_file.
        :param response: The response to get cookies from, dict.
        """
        # Extract cookies from the response
        self.cookies = response.get('cookies')
        # Save the cookies to the file
        self._save_cookies()

    def load_cookies(self):
        """
        Loads the cookies from the cookies_file to the cookies data.
        :return: The cookies data, dict.
        """
        try:
            # Open the cookies file and load the data
            with open(self.cookies_file, 'r') as file:
                self.cookies = json.load(file)
            return self.cookies
        except FileNotFoundError:
            # If the file does not exist, return an empty dictionary
            return {}
        except json.JSONDecodeError:
            # If the file is not a valid JSON, return an empty dictionary
            return {}

    def _save_cookies(self):
        """
        Saves the cookies to the cookies_file, and returns True if successful, False otherwise.
        :return: True if successful, False otherwise.
        """
        try:
            # Open the cookies file and save the data
            with open(self.cookies_file, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except Exception as e:
            # If an error occurs, print the error and return False
            print(f"Error saving cookies: {e}")
            return False