import logging
import datetime
import jwt  # Assuming JWT is used for token parsing

class AccessGatewayFilter:
    def __init__(self):
        self.logger = logging.getLogger('AccessGatewayFilter')
        self.allowed_prefixes = ['/api', '/public']  # Example allowed prefixes

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: The incoming request object
        :return: bool, True if the request is allowed, False otherwise
        """
        request_uri = request.get('uri', '')
        
        # Check if the request URI starts with allowed prefixes
        if not self.is_start_with(request_uri):
            self.logger.warning(f"Request URI {request_uri} not allowed.")
            return False
        
        # Extract and validate JWT token
        user_info = self.get_jwt_user(request)
        if user_info is None:
            self.logger.warning("Invalid or missing JWT token.")
            return False
        
        # Set the user info and log the access
        self.set_current_user_info_and_log(user_info)
        
        return True

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: The URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        for prefix in self.allowed_prefixes:
            if request_uri.startswith(prefix):
                return True
        return False

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: The incoming request object
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        token = request.get('headers', {}).get('Authorization', '').replace('Bearer ', '')
        if not token:
            return None
        
        try:
            # Decode the JWT token (assuming a secret key is used for encoding)
            decoded_token = jwt.decode(token, 'your-secret-key', algorithms=['HS256'])
            return decoded_token.get('user')
        except jwt.ExpiredSignatureError:
            self.logger.warning("JWT token has expired.")
        except jwt.InvalidTokenError:
            self.logger.warning("Invalid JWT token.")
        
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: The user information dictionary
        :return: None
        """
        # Example: setting user info in a session or context
        self.logger.info(f"User {user.get('username')} accessed the system at {datetime.datetime.now()}.")