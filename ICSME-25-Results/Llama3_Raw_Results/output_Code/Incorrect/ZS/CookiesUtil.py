import json

class CookiesUtil:
    def __init__(self, cookies_file):
        # Initialize the cookies file path
        self.cookies_file = cookies_file
        # Initialize the cookies data as an empty dictionary
        self.cookies_data = {}

    def get_cookies(self, response):
        # Get the cookies from the response
        self.cookies_data = response.cookies.get_dict()
        # Save the cookies to the cookies file
        self._save_cookies()

    def load_cookies(self):
        # Try to load the cookies from the cookies file
        try:
            with open(self.cookies_file, 'r') as file:
                # Load the cookies data from the file
                self.cookies_data = json.load(file)
        except FileNotFoundError:
            # If the file does not exist, return an empty dictionary
            self.cookies_data = {}
        # Return the cookies data
        return self.cookies_data

    def _save_cookies(self):
        # Try to save the cookies to the cookies file
        try:
            with open(self.cookies_file, 'w') as file:
                # Save the cookies data to the file
                json.dump(self.cookies_data, file)
            # Return True if successful
            return True
        except Exception as e:
            # Print the error message
            print(f"Error saving cookies: {e}")
            # Return False if failed
            return False