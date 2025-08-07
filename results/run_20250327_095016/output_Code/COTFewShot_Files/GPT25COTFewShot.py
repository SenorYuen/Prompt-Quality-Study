import json

class CookiesUtil:
    def __init__(self, cookies_file):
        self.cookies_file = cookies_file
        self.cookies = None

    def get_cookies(self, response):
        self.cookies = response.get('cookies', {})
        self._save_cookies()

    def load_cookies(self):
        try:
            with open(self.cookies_file, 'r') as file:
                self.cookies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.cookies = {}
        return self.cookies

    def _save_cookies(self):
        try:
            with open(self.cookies_file, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except:
            return False