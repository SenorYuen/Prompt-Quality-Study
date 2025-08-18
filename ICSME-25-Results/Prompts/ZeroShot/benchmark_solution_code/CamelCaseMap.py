'''
# This is a custom class that allows keys to be in camel case style by converting them from underscore style, which provides dictionary-like functionality.

class CamelCaseMap:
    def __init__(self):
        """
        Initialize data to an empty dictionary
        """

    def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :return:str,the value corresponding to the key
        """


    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :return:None
        """


    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :return:None
        """


    def __iter__(self):
        """
        Returning Iterateable Objects with Own Data
        :return:Iterator
        """


    def __len__(self):
        """
        Returns the length of the own data
        :return:int, length of data
        """

    def _convert_key(self, key):
        """
        convert key string into camel case
        :return:str, converted key string
        """

    @staticmethod
    def _to_camel_case(key):
        """
        convert key string into camel case
        :return:str, converted key string
        """

'''


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
        if isinstance(key, str):
            return self._to_camel_case(key)
        return key

    @staticmethod
    def _to_camel_case(key):
        parts = key.split('_')
        return parts[0] + ''.join(part.title() for part in parts[1:])


