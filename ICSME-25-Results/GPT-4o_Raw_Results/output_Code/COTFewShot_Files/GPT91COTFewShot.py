import urllib.parse

class UrlPath:
    def __init__(self):
        self.segments = []
        self.with_end_tag = False

    def add(self, segment):
        self.segments.append(segment)

    def parse(self, path, charset):
        path = self.fix_path(path)
        self.segments = [urllib.parse.unquote(segment, encoding=charset) for segment in path.split('/') if segment]

    @staticmethod
    def fix_path(path):
        return path.strip('/')