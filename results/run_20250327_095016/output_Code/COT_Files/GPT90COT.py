class URLHandler:
    def __init__(self, url):
        self.url = url

    def get_scheme(self):
        return self.url.split("://")[0]

    def get_host(self):
        return self.url.split("://")[1].split("/")[0]

    def get_path(self):
        return '/' + '/'.join(self.url.split("://")[1].split("/")[1:]).split('?')[0]

    def get_query_params(self):
        query_string = self.url.split('?')[1].split('#')[0]
        params = query_string.split('&')
        return {param.split('=')[0]: param.split('=')[1] for param in params}

    def get_fragment(self):
        return self.url.split('#')[1]