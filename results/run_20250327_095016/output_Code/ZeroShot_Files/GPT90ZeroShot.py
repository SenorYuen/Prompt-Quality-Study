from urllib.parse import urlparse, parse_qs

class URLHandler:
    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        # Parse the URL using urlparse and store the result
        self.parsed_url = urlparse(url)

    def get_scheme(self):
        """
        Get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        """
        # Return the scheme part of the parsed URL
        return self.parsed_url.scheme

    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        """
        # Return the netloc part of the parsed URL, which represents the host
        return self.parsed_url.netloc

    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        """
        # Return the path part of the parsed URL
        return self.parsed_url.path

    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        """
        # Parse the query part of the parsed URL into a dictionary
        return parse_qs(self.parsed_url.query)

    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        """
        # Return the fragment part of the parsed URL
        return self.parsed_url.fragment