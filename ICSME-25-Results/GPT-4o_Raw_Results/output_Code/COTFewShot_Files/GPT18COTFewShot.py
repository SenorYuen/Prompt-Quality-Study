class CamelCaseMap:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        camel_key = self._convert_key(key)
        return self._data[camel_key]

    def __setitem__(self, key, value):
        camel_key = self._convert_key(key)
        self._data[camel_key] = value

    def __delitem__(self, key):
        camel_key = self._convert_key(key)
        del self._data[camel_key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def _convert_key(self, key):
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        parts = key.split('_')
        return parts[0] + ''.join(part.capitalize() for part in parts[1:])