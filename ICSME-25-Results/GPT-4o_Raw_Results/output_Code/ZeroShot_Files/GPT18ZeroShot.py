class CamelCaseMap:
    def __init__(self):
        """
        Initialize data to an empty dictionary
        """
        self.data = {}

    def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :return: str, the value corresponding to the key
        """
        camel_case_key = self._convert_key(key)
        return self.data[camel_case_key]

    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :return: None
        """
        camel_case_key = self._convert_key(key)
        self.data[camel_case_key] = value

    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :return: None
        """
        camel_case_key = self._convert_key(key)
        del self.data[camel_case_key]

    def __iter__(self):
        """
        Returning Iterable Objects with Own Data
        :return: Iterator
        """
        return iter(self.data)

    def __len__(self):
        """
        Returns the length of the own data
        :return: int, length of data
        """
        return len(self.data)

    def _convert_key(self, key):
        """
        Convert key string into camel case
        :return: str, converted key string
        """
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        """
        Convert key string into camel case
        :return: str, converted key string
        """
        parts = key.split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])