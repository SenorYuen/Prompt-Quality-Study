import json
import os

class JSONProcessor:
    """
    This is a class to process JSON file, including reading and writing JSON files, as well as processing JSON data by removing a specified key from the JSON object.
    """

    def read_json(self, file_path):
        # Check if the file exists
        if not os.path.exists(file_path):
            return 0
        
        try:
            # Attempt to open and read the JSON file
            with open(file_path, 'r') as file:
                # Load the JSON data
                data = json.load(file)
                return data
        except:
            # Return -1 if an error occurs during the reading process
            return -1

    def write_json(self, data, file_path):
        try:
            # Attempt to write the data to the JSON file
            with open(file_path, 'w') as file:
                # Dump the JSON data
                json.dump(data, file)
                return 1
        except:
            # Return -1 if an error occurs during the writing process
            return -1

    def process_json(self, file_path, remove_key):
        # Read the JSON file
        data = self.read_json(file_path)
        
        # Check if the file does not exist or an error occurred
        if data == 0 or data == -1:
            return 0
        
        # Check if the key exists in the data
        if remove_key not in data:
            return 0
        
        # Remove the specified key from the data
        del data[remove_key]
        
        # Write the modified data back to the file
        result = self.write_json(data, file_path)
        
        # Return 1 if the writing process is successful
        if result == 1:
            return 1
        else:
            return 0