# This is a custom class that allows keys to be in camel case style by converting them from underscore style, 
# which provides dictionary-like functionality.

class CamelCaseMap:
    def __init__(self):
        # Initialize data to an empty dictionary
        self.data = {}

    def __getitem__(self, key):
        # Convert key to camel case and return the value corresponding to the key
        return self.data[self._convert_key(key)]

    def __setitem__(self, key, value):
        # Convert key to camel case and set the value corresponding to the key to the specified value
        self.data[self._convert_key(key)] = value

    def __delitem__(self, key):
        # Convert key to camel case and delete the value corresponding to the key
        del self.data[self._convert_key(key)]

    def __iter__(self):
        # Returning Iterateable Objects with Own Data
        return iter(self.data)

    def __len__(self):
        # Returns the length of the own data
        return len(self.data)

    def _convert_key(self, key):
        # Convert key string into camel case
        return self._to_camel_case(key)

    @staticmethod
    def _to_camel_case(key):
        # Split key by underscore and capitalize the first letter of each word except the first word
        words = key.split('_')
        # Capitalize the first letter of each word except the first word
        camel_case_key = words[0] + ''.join(word.capitalize() for word in words[1:])
        return camel_case_key

# Example usage
if __name__ == "__main__":
    camel_case_map = CamelCaseMap()
    camel_case_map['hello_world'] = 'Hello World'
    print(camel_case_map['hello_world'])  # Outputs: Hello World
    print(len(camel_case_map))  # Outputs: 1
    for key in camel_case_map:
        print(key)  # Outputs: helloWorld
    del camel_case_map['hello_world']
    print(len(camel_case_map))  # Outputs: 0