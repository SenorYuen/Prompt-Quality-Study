class URLHandler:
    def __init__(self, url):
        self.url = url

    def _get_scheme(self):
        return self.url.split('://')[0]

    def get_host(self):
        return self.url.split('://')[1].split('/')[0]

    def get_path(self):
        path = self.url.split('://')[1].split('/', 1)
        if len(path) > 1:
            return '/' + path[1]
        else:
            return ''

    def get_query_params(self):
        query = self.url.split('?')
        if len(query) > 1:
            params = query[1].split('#')[0].split('&')
            query_params = {}
            for param in params:
                key_value = param.split('=')
                if len(key_value) > 1:
                    query_params[key_value[0]] = key_value[1]
            return query_params
        else:
            return {}

    def get_fragment(self):
        fragment = self.url.split('#')
        if len(fragment) > 1:
            return fragment[1]
        else:
            return ''

    def get_scheme(self):
        return self._get_scheme()