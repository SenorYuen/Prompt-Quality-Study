import logging
import jwt
from datetime import date

class AccessGatewayFilter:
    def __init__(self):
        pass

    def filter(self, request):
        # Filter incoming requests based on certain rules and conditions
        if request['path'] == '/login' and request['method'] == 'POST':
            return True
        else:
            # Add additional filtering logic as needed
            return False

    def is_start_with(self, request_uri):
        # Check if the request URI starts with certain prefixes
        prefixes = ['/api/data', '/api/auth']
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                return True
        return False

    def get_jwt_user(self, request):
        # Get the user information from the JWT token in the request
        try:
            token = request['headers']['Authorization']['jwt']
            user_info = jwt.decode(token, options={"verify_signature": False})
            return user_info
        except:
            return None

    def set_current_user_info_and_log(self, user):
        # Set the current user information and log the access
        logging.info(f"User {user['name']} accessed the system from {user.get('address', 'unknown')}")
        # Add additional logging or user information setting logic as needed
        pass