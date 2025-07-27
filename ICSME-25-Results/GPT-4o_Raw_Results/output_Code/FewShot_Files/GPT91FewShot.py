import urllib.parse

class UrlPath:
    """
    The UrlPath class is a utility for encapsulating and manipulating the path component of a URL, including adding nodes, parsing path strings, and building path strings with optional encoding.
    """

    def __init__(self):
        """
        Initializes the UrlPath object with an empty list of segments and a flag indicating the presence of an end tag.
        """
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        """
        Adds a segment to the list of segments in the UrlPath.
        :param segment: str, the segment to add.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')

        url_path.segments = ['foo', 'bar']
        """
        # Add the segment to the segments list
        self.segments.append(segment)

    def parse(self, path, charset='utf-8'):
        """
        Parses a given path string and populates the list of segments in the UrlPath.
        :param path: str, the path string to parse.
        :param charset: str, the character encoding of the path string.
        >>> url_path = UrlPath()
        >>> url_path.parse('/foo/bar/', 'utf-8')

        url_path.segments = ['foo', 'bar']
        """
        # Fix the path to remove leading and trailing slashes
        fixed_path = self.fix_path(path)
        # Decode the path using the specified charset
        decoded_path = urllib.parse.unquote(fixed_path, encoding=charset)
        # Split the path into segments and set it to self.segments
        self.segments = decoded_path.split('/')
        # Check if the original path had a trailing slash to set the end tag flag
        self.with_end_tag = path.endswith('/')

    @staticmethod
    def fix_path(path):
        """
        Fixes the given path string by removing leading and trailing slashes.
        :param path: str, the path string to fix.
        :return: str, the fixed path string.
        >>> url_path = UrlPath()
        >>> url_path.fix_path('/foo/bar/')
        'foo/bar'
        """
        # Strip leading and trailing slashes from the path
        return path.strip('/')

    def build(self, charset='utf-8'):
        """
        Builds the path string from the list of segments with optional encoding.
        :param charset: str, the character encoding to use when encoding the path string.
        :return: str, the constructed path string.
        >>> url_path = UrlPath()
        >>> url_path.add('foo')
        >>> url_path.add('bar')
        >>> url_path.build()
        '/foo/bar/'
        """
        # Join the segments into a single path string
        path = '/'.join(self.segments)
        # Encode the path using the specified charset
        encoded_path = urllib.parse.quote(path, encoding=charset)
        # Add leading and possibly trailing slashes
        if self.with_end_tag:
            return f'/{encoded_path}/'
        else:
            return f'/{encoded_path}'