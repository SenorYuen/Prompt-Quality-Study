import json
import os

class JSONProcessor:
    """
    This is a class to process JSON file, including reading and writing JSON files, as well as processing JSON data by removing a specified key from the JSON object.
    """

    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        :param file_path: str, the path of the JSON file.
        :return: dict, the data from the JSON file if read successfully, or return -1 if an error occurs during the reading process.
                    return 0 if the file does not exist.
        >>> json_processor = JSONProcessor()
        >>> json_processor.read_json('test.json')
        {'name': 'test', 'age': 14}
        """
        # Check if the file exists
        if not os.path.exists(file_path):
            return 0
        try:
            # Open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except:
            # Return -1 if an error occurs during reading
            return -1

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.

        :param data: dict, the data to be written to the JSON file.
        :param file_path: str, the path of the JSON file.
        :return: 1 if the writing process is successful, or -1, if an error occurs during the writing process.
        >>> json_processor = JSONProcessor()
        >>> json_processor.write_json({'key1': 'value1', 'key2': 'value2'}, 'test.json')
        1
        >>> json_processor.read_json('test.json')
        {'key1': 'value1', 'key2': 'value2'}
        """
        try:
            # Open the file in write mode and dump the JSON data into it
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return 1
        except:
            # Return -1 if an error occurs during writing
            return -1

    def process_json(self, file_path, remove_key):
        """
        Read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.

        :param file_path: str, the path of the JSON file.
        :param remove_key: str, the key to be removed.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        >>> json_processor = JSONProcessor()
        >>> json_processor.read_json('test.json')
        {'key1': 'value1', 'key2': 'value2'}
        >>> json_processor.process_json('test.json', 'key1')
        1
        >>> json_processor.read_json('test.json')
        {'key2': 'value2'}
        """
        # Read the JSON data from the file
        data = self.read_json(file_path)
        if data == 0 or data == -1:
            return 0
        
        # Check if the key exists in the data
        if remove_key in data:
            # Remove the specified key
            del data[remove_key]
            # Write the modified data back to the file
            if self.write_json(data, file_path) == 1:
                return 1
        return 0