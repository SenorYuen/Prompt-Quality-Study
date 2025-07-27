# Import the required library for parsing URLs
from urllib.parse import urlparse, parse_qs

class URLHandler:
    def __init__(self, url):
        # Initialize URLHandler's URL by parsing it into its components
        self.parsed_url = urlparse(url)

    def get_scheme(self):
        # Get the scheme of the URL from the parsed URL
        return self.parsed_url.scheme

    def get_host(self):
        # Get the host domain name of the URL from the parsed URL
        return self.parsed_url.netloc

    def get_path(self):
        # Get the address of the resource of the URL from the parsed URL
        return self.parsed_url.path

    def get_query_params(self):
        # Get the request parameters of the URL from the parsed URL
        # and parse them into a dictionary
        return parse_qs(self.parsed_url.query)

    def get_fragment(self):
        # Get the fragment after '#' of the URL from the parsed URL
        return self.parsed_url.fragment

# Example usage:
if __name__ == "__main__":
    url = "https://www.example.com/path/to/resource?param1=value1&param2=value2#fragment"
    handler = URLHandler(url)
    print("Scheme:", handler.get_scheme())
    print("Host:", handler.get_host())
    print("Path:", handler.get_path())
    print("Query Parameters:", handler.get_query_params())
    print("Fragment:", handler.get_fragment())