class CamelCaseMap:
    """
    This is a custom class that allows keys to be in camel case style by converting them from underscore style, which provides dictionary-like functionality.
    """

    def __init__(self):
        """
        Initialize data to an empty dictionary
        """
        self._data = {}

    def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :param key: str
        :return: str, the value corresponding to the key
        """
        # Convert the key to camel case before fetching the value
        camel_case_key = self._convert_key(key)
        return self._data[camel_case_key]

    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key: str
        :param value: str, the specified value
        :return: None
        """
        # Convert the key to camel case before setting the value
        camel_case_key = self._convert_key(key)
        self._data[camel_case_key] = value

    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key: str
        :return: None
        """
        # Convert the key to camel case before deleting the item
        camel_case_key = self._convert_key(key)
        del self._data[camel_case_key]

    def __iter__(self):
        """
        Returning Iterable Objects with Own Data
        :return: Iterator
        """
        # Return iterator over the keys of the data dictionary
        return iter(self._data)

    def __len__(self):
        """
        Returns the length of the own data
        :return: int, length of data
        """
        # Return the length of the data dictionary
        return len(self._data)

    def _convert_key(self, key):
        """
        Convert key string into camel case
        :param key: str
        :return: str, converted key string
        """
        # Use the static method to convert the key to camel case
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        """
        Convert key string into camel case
        :param key: str
        :return: str, converted key string
        """
        # Split the key by underscores
        parts = key.split('_')
        # Capitalize the first letter of each part except the first one and join them back
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])