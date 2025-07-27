import urllib.parse

class UrlPath:
    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments.
        """
        self.segments = []

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        """
        # Append the segment to the segments list
        self.segments.append(segment)

    def parse(self, path, charset='utf-8'):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character set for decoding the path.
        """
        # Fix the path by removing leading and trailing slashes
        fixed_path = self.fix_path(path)
        # Split the fixed path into segments
        segments = fixed_path.split('/')
        # Decode each segment and add it to the segments list
        for segment in segments:
            self.segments.append(urllib.parse.unquote(segment, encoding=charset))

    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path to fix.
        :return: str, the fixed path string.
        """
        # Strip leading and trailing slashes from the path
        return path.strip('/')