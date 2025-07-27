# This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.
import logging
import datetime
import jwt  # Import the PyJWT library for handling JWT tokens

class AccessGatewayFilter:
    def __init__(self):
        # Initialize the logger
        self.logger = logging.getLogger(__name__)
        # Set the secret key for JWT token verification
        self.secret_key = "your_secret_key_here"

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :return: bool, True if the request is allowed, False otherwise
        """
        # Check if the request URI starts with certain prefixes
        if not self.is_start_with(request.uri):
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
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """
        # Define the allowed prefixes
        allowed_prefixes = ["/api", "/admin"]
        for prefix in allowed_prefixes:
            if request_uri.startswith(prefix):
                return True
        return False

    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :return: dict or None, the user information if the token is valid, None otherwise
        """
        # Get the JWT token from the request headers
        token = request.headers.get("Authorization")
        if token is None:
            return None
        
        # Verify the JWT token
        try:
            user = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return user
        except jwt.ExpiredSignatureError:
            self.logger.warning("Expired JWT token")
        except jwt.InvalidTokenError:
            self.logger.warning("Invalid JWT token")
        return None

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :return: None
        """
        # Set the current user information
        self.current_user = user
        # Log the access
        self.logger.info(f"Access logged for user {user['username']} at {datetime.datetime.now()}")