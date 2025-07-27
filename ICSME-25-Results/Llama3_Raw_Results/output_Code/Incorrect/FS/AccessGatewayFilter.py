import logging
import datetime
import jwt  # assuming you're using PyJWT library

class AccessGatewayFilter:
    """
    This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
    """

    def __init__(self):
        # Initialize the logger
        self.logger = logging.getLogger(__name__)

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :param request: dict, the incoming request details
        :return: bool, True if the request is allowed, False otherwise
        """
        # Check if the request path starts with certain prefixes
        if not self.is_start_with(request['path']):
            return False
        
        # Get the user information from the JWT token in the request
        user = self.get_jwt_user(request)
        if user is None:
            return False
        
        # Set the current user information and log the access
        self.set_current_user_info_and_log(user)
        
        return True

    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :param request_uri: str, the URI of the request
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        # Define the allowed prefixes
        allowed_prefixes = ['/api', '/login']
        
        # Check if the request URI starts with any of the allowed prefixes
        for prefix in allowed_prefixes:
            if request_uri.startswith(prefix):
                return True
        
        return False

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :param request: dict, the incoming request details
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        # Get the JWT token from the request headers
        token = request.get('headers', {}).get('Authorization', {}).get('jwt')
        
        # Check if the token is valid
        if token is None:
            return None
        
        try:
            # Decode the JWT token
            user = jwt.decode(token, options={'verify_signature': False})
            return user
        except jwt.ExpiredSignatureError:
            # Handle expired token
            self.logger.warning('Expired JWT token')
            return None
        except jwt.InvalidTokenError:
            # Handle invalid token
            self.logger.warning('Invalid JWT token')
            return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :param user: dict, the user information
        :return: None
        """
        # Set the current user information
        self.current_user = user
        
        # Log the access
        self.logger.info(f'Access logged for user {user["name"]}')