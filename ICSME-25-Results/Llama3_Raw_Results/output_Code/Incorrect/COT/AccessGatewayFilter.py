import logging
from datetime import datetime

class AccessGatewayFilter:
    def __init__(self):
        # Initialize the logger
        self.logger = logging.getLogger(__name__)

    def filter(self, request: dict) -> bool:
        # Check if the request path starts with '/api' or '/login'
        if self.is_start_with(request.get('path', '')):
            # If the request path starts with '/api' or '/login', check if the request method is 'POST' or 'GET'
            if request.get('method', '') in ['POST', 'GET']:
                # If the request method is 'POST' or 'GET', return True
                return True
        # If none of the above conditions are met, return False
        return False

    def is_start_with(self, request_uri: str) -> bool:
        # Define the prefixes to check
        prefixes = ['/api', '/login']
        # Check if the request URI starts with any of the prefixes
        for prefix in prefixes:
            if request_uri.startswith(prefix):
                # If the request URI starts with any of the prefixes, return True
                return True
        # If none of the prefixes match, return False
        return False

    def get_jwt_user(self, request: dict) -> dict:
        # Get the JWT token from the request headers
        jwt_token = request.get('headers', {}).get('Authorization', {}).get('jwt')
        # Get the user information from the JWT token
        user_info = request.get('headers', {}).get('Authorization', {}).get('user')
        # If the JWT token is valid, return the user information
        if jwt_token and user_info:
            return user_info
        # If the JWT token is not valid, return None
        return None

    def set_current_user_info_and_log(self, user: dict) -> None:
        # Set the current user information
        self.current_user = user
        # Log the access
        self.logger.info(f'User {user.get("name")} accessed from {user.get("address")}')
        # Log the access with timestamp
        self.logger.info(f'Access logged at {datetime.now()}')