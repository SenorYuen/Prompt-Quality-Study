import urllib.parse

class UrlPath:
    def __init__(self, url=None):
        self.segments = []
        self.with_end_tag = False
        if url:
            self.parse(url, 'utf-8')

    def add(self, segment):
        self.segments.append(segment)

    def parse(self, path, charset):
        fixed_path = UrlPath.fix_path(path)
        self.segments = fixed_path.split('/')

    @staticmethod
    def fix_path(path):
        return path.strip('/')

# Example usage
url_path = UrlPath()
url_path.add('foo')
url_path.add('bar')
print(url_path.segments)  # Output: ['foo', 'bar']

url_path = UrlPath()
url_path.parse('/foo/bar/', 'utf-8')
print(url_path.segments)  # Output: ['foo', 'bar']

url_path = UrlPath()
print(UrlPath.fix_path('/foo/bar/'))  # Output: 'foo/bar'