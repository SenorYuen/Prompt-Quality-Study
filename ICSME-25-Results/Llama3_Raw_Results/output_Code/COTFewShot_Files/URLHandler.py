class URLHandler:
    def __init__(self, url):
        self.url = url

    def _get_scheme(self):
        return self.url.split('://')[0]

    def get_host(self):
        url_parts = self.url.split('://')
        if len(url_parts) > 1:
            host_path = url_parts[1].split('/')
            return host_path[0]
        else:
            return None

    def get_path(self):
        url_parts = self.url.split('://')
        if len(url_parts) > 1:
            host_path = url_parts[1].split('/', 1)
            if len(host_path) > 1:
                return '/' + host_path[1]
            else:
                return '/'
        else:
            return self.url

    def get_query_params(self):
        url_parts = self.url.split('?')
        if len(url_parts) > 1:
            query_params = url_parts[1].split('#')[0]
            params_dict = {}
            for param in query_params.split('&'):
                key_value = param.split('=')
                if len(key_value) == 2:
                    params_dict[key_value[0]] = key_value[1]
            return params_dict
        else:
            return {}

    def get_fragment(self):
        url_parts = self.url.split('#')
        if len(url_parts) > 1:
            return url_parts[1]
        else:
            return None

    def get_scheme(self):
        return self._get_scheme()