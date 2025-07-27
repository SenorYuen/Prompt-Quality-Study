class URLHandler:
    def __init__(self, url):
        self.url = url

    def get_scheme(self):
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            return self.url[:scheme_end]
        return ""

    def get_host(self):
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            host_start = scheme_end + 3
            host_end = self.url.find("/", host_start)
            if host_end == -1:
                host_end = len(self.url)
            return self.url[host_start:host_end]
        return ""

    def get_path(self):
        scheme_end = self.url.find("://")
        if scheme_end != -1:
            host_start = scheme_end + 3
            path_start = self.url.find("/", host_start)
            if path_start != -1:
                return self.url[path_start:]
        return ""

    def get_query_params(self):
        query_start = self.url.find("?")
        fragment_start = self.url.find("#")
        if query_start != -1:
            query_end = fragment_start if fragment_start != -1 else len(self.url)
            query_string = self.url[query_start + 1:query_end]
            params = {}
            for param in query_string.split("&"):
                key_value = param.split("=")
                if len(key_value) == 2:
                    params[key_value[0]] = key_value[1]
            return params
        return {}

    def get_fragment(self):
        fragment_start = self.url.find("#")
        if fragment_start != -1:
            return self.url[fragment_start + 1:]
        return ""