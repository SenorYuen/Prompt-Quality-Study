'''
# This class is a filter used for accessing gateway filtering, primarily for authentication and access log recording.

import logging
import datetime

class AccessGatewayFilter:
    def __init__(self):
        pass

    def filter(self, request):
        """
        Filter the incoming request based on certain rules and conditions.
        :return: bool, True if the request is allowed, False otherwise
        """


    def is_start_with(self, request_uri):
        """
        Check if the request URI starts with certain prefixes.
        :return: bool, True if the URI starts with certain prefixes, False otherwise
        """


    def get_jwt_user(self, request):
        """
        Get the user information from the JWT token in the request.
        :return: dict or None, the user information if the token is valid, None otherwise
        """

    def set_current_user_info_and_log(self, user):
        """
        Set the current user information and log the access.
        :return: None
        """

'''

import logging
import datetime


class AccessGatewayFilter:

    def __init__(self):
        pass

    def filter(self, request):
        request_uri = request['path']
        method = request['method']

        if self.is_start_with(request_uri):
            return True

        try:
            token = self.get_jwt_user(request)
            user = token['user']
            if user['level'] > 2:
                self.set_current_user_info_and_log(user)
                return True
        except:
            return False

    def is_start_with(self, request_uri):
        start_with = ["/api", '/login']
        for s in start_with:
            if request_uri.startswith(s):
                return True
        return False

    def get_jwt_user(self, request):
        token = request['headers']['Authorization']
        user = token['user']
        if token['jwt'].startswith(user['name']):
            jwt_str_date = token['jwt'].split(user['name'])[1]
            jwt_date = datetime.datetime.strptime(jwt_str_date, "%Y-%m-%d")
            if datetime.datetime.today() - jwt_date >= datetime.timedelta(days=3):
                return None
        return token

    def set_current_user_info_and_log(self, user):
        host = user['address']
        logging.log(msg=user['name'] + host + str(datetime.datetime.now()), level=1)
