import logging
import datetime

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        # Initialize the logger
        self.logger = logging.getLogger('AccessGatewayFilter')
        self.logger.setLevel(logging.INFO)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        # Check if the request path is allowed
        if self.is_start_with(request.get('path', '')):
            # Get the user from JWT token
            user = self.get_jwt_user(request)
            if user:
                # Log the user information
                self.set_current_user_info_and_log(user)
                return True
        return False

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        # Define allowed prefixes
        allowed_prefixes = ['/api', '/login']
        # Check if the request URI starts with any of the allowed prefixes
        return any(request_uri.startswith(prefix) for prefix in allowed_prefixes)

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        # Extract the Authorization header
        auth_header = request.get('headers', {}).get('Authorization', {})
        # Validate the JWT token (mock validation for example purposes)
        jwt_token = auth_header.get('jwt', '')
        if jwt_token and jwt_token.endswith(str(datetime.date.today())):
            # Return user information if the token is valid
            return auth_header.get('user', None)
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        # Log the user access
        self.logger.info(f"User {user.get('name')} accessed from {user.get('address', 'unknown address')}")