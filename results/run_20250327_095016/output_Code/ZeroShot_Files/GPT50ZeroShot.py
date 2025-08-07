import json
import os

class JSONProcessor:
    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        :return: dict, the data from the JSON file if read successfully, or return -1 if an error occurs during the reading process.
                    return 0 if the file does not exist.
        """
        if not os.path.exists(file_path):
            return 0  # File does not exist
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return -1  # Error during reading

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.
        :return: 1 if the writing process is successful, or -1, if an error occurs during the writing process.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return 1  # Writing successful
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
            return -1  # Error during writing

    def process_json(self, file_path, remove_key):
        """
        Read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        """
        data = self.read_json(file_path)
        if data == 0:
            return 0  # File does not exist
        if data == -1:
            return -1  # Error during reading

        if remove_key in data:
            del data[remove_key]
            write_status = self.write_json(data, file_path)
            if write_status == 1:
                return 1  # Key removed and data written back successfully
            else:
                return -1  # Error during writing
        else:
            return 0  # Specified key does not exist