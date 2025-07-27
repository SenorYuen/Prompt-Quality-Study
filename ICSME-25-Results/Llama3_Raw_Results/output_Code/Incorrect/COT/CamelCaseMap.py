class CamelCaseMap:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[self._convert_key(key)]

    def __setitem__(self, key, value):
        self._data[self._convert_key(key)] = value

    def __delitem__(self, key):
        del self._data[self._convert_key(key)]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def _convert_key(self, key):
        return CamelCaseMap._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        words = key.split('_')
        return words[0] + ''.join(word.capitalize() for word in words[1:])