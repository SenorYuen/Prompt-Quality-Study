import datetime

class AccessGatewayFilter:
    def __init__(self):
        pass

    def filter(self, request):
        if self.is_start_with(request['path']):
            return True
        user = self.get_jwt_user(request)
        if user:
            self.set_current_user_info_and_log(user)
            return True
        return False

    def is_start_with(self, request_uri):
        allowed_prefixes = ['/api', '/login', '/public']
        return any(request_uri.startswith(prefix) for prefix in allowed_prefixes)

    def get_jwt_user(self, request):
        auth_header = request.get('headers', {}).get('Authorization', None)
        if auth_header:
            token = auth_header.get('jwt', None)
            if token and token.endswith(str(datetime.date.today())):
                return auth_header.get('user', None)
        return None

    def set_current_user_info_and_log(self, user):
        # Assuming user is a dictionary with user information
        print(f"User {user.get('name')} accessed the system.")
        # Additional logging can be implemented here