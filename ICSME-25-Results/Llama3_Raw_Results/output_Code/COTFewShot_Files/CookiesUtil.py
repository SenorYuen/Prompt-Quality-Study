import json

class CookiesUtil:
    def __init__(self, cookies_file):
        self.cookies_file = cookies_file
        self.cookies = None

    def get_cookies(self, response):
        if 'cookies' in response:
            self.cookies = response['cookies']
            self._save_cookies()
            return self.cookies
        else:
            return None

    def load_cookies(self):
        try:
            with open(self.cookies_file, 'r') as file:
                self.cookies = json.load(file)
            return self.cookies
        except FileNotFoundError:
            return None
        except json.JSONDecodeError:
            return None

    def _save_cookies(self):
        if self.cookies is not None:
            try:
                with open(self.cookies_file, 'w') as file:
                    json.dump(self.cookies, file)
                return True
            except Exception as e:
                print(f"Error saving cookies: {e}")
                return False
        else:
            return False