from urllib.parse import urlparse, parse_qs

class URLHandler:
    """
    The class supports to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        self.url = url

    # Get the scheme of the URL
    def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        """
        # Use urlparse to break the URL into its components
        parsed_url = urlparse(self.url)
        # Return the scheme
        return parsed_url.scheme

    # Get the host domain name of the URL
    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        """
        # Use urlparse to break the URL into its components
        parsed_url = urlparse(self.url)
        # Return the hostname
        return parsed_url.hostname

    # Get the path of the URL
    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        """
        # Use urlparse to break the URL into its components
        parsed_url = urlparse(self.url)
        # Return the path
        return parsed_url.path

    # Get the query parameters of the URL
    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        """
        # Use urlparse to break the URL into its components
        parsed_url = urlparse(self.url)
        # Use parse_qs to parse the query string into a dictionary
        query_params = parse_qs(parsed_url.query)
        # Return the query parameters
        return query_params

    # Get the fragment of the URL
    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        """
        # Use urlparse to break the URL into its components
        parsed_url = urlparse(self.url)
        # Return the fragment
        return parsed_url.fragment