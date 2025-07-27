import datetime

class AccessGatewayFilter:
    def __init__(self):
        pass

    def filter(self, request):
        if self.is_start_with(request.get('path', '')):
            return True
        user_info = self.get_jwt_user(request)
        if user_info:
            self.set_current_user_info_and_log(user_info)
            return True
        return False

    def is_start_with(self, request_uri):
        prefixes = ['/api', '/auth', '/public']
        return any(request_uri.startswith(prefix) for prefix in prefixes)

    def get_jwt_user(self, request):
        auth_header = request.get('headers', {}).get('Authorization', {})
        if isinstance(auth_header, dict) and 'user' in auth_header and 'jwt' in auth_header:
            expected_jwt = auth_header['user']['name'] + str(datetime.date.today())
            if auth_header['jwt'] == expected_jwt:
                return auth_header['user']
        return None

    def set_current_user_info_and_log(self, user):
        # Assuming there is a logging mechanism
        print(f"User {user['name']} accessed from {user.get('address', 'unknown')}")