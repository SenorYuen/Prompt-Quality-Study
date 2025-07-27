import urllib.parse

class UrlPath:
    """
    The  class is a utility for encapsulating and manipulating the path component of a URL, including adding nodes, parsing path strings, and building path strings with optional encoding.
    """

    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments and a flag indicating the presence of an end tag.
        """
        # Initialize an empty list to store the path segments
        self.segments = []
        # Initialize a flag to track if an end tag is present
        self.with_end_tag = False

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        """
        # Append the segment to the list of segments
        self.segments.append(segment)

    def parse(self, path, charset):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        """
        # Remove leading and trailing slashes from the path
        path = self.fix_path(path)
        # Split the path into segments using '/' as the separator
        segments = path.split('/')
        # Iterate over each segment and add it to the list of segments
        for segment in segments:
            # Check if the segment is not empty
            if segment:
                # Unquote the segment to decode any URL-encoded characters
                segment = urllib.parse.unquote(segment)
                # Add the segment to the list of segments
                self.add(segment)

    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        """
        # Remove leading slashes from the path
        path = path.lstrip('/')
        # Remove trailing slashes from the path
        path = path.rstrip('/')
        # Return the fixed path
        return path