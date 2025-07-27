import urllib.parse

class UrlPath:
    def __init__(self):
        # Initialize the UrlPath object with an empty list of segments and a flag indicating the presence of an end tag.
        self.segments = []
        self.has_end_tag = False

    def add(self, segment):
        # Adds a segment to the list of segments in the UrlPath.
        # Ensure the segment is not empty and does not contain any invalid characters.
        if segment:
            self.segments.append(urllib.parse.quote(segment))

    def parse(self, path, charset):
        # Parses a given path string and populates the list of segments in the UrlPath.
        # Remove leading and trailing slashes from the path.
        fixed_path = UrlPath.fix_path(path)
        # Split the path into segments.
        self.segments = [urllib.parse.quote(segment, encoding=charset) for segment in fixed_path.split('/') if segment]

    @staticmethod
    def fix_path(path):
        # Fixes the given path string by removing leading and trailing slashes.
        # Remove leading slashes.
        while path.startswith('/'):
            path = path[1:]
        # Remove trailing slashes.
        while path.endswith('/'):
            path = path[:-1]
        return path

    def build(self, charset):
        # Builds the path string from the list of segments in the UrlPath.
        # Join the segments with slashes.
        path = '/'.join(self.segments)
        # If the path is not empty, add a leading slash.
        if path:
            path = '/' + path
        # If the has_end_tag flag is True, append a slash at the end of the path.
        if self.has_end_tag and path:
            path += '/'
        return path

    def __str__(self):
        # Returns the string representation of the UrlPath object.
        return self.build('utf-8')