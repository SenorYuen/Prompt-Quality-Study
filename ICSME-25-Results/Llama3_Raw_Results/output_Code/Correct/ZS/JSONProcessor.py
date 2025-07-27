# This is a class to process JSON file, including reading and writing JSON files, as well as processing JSON data by removing a specified key from the JSON object.

import json
import os

class JSONProcessor:
    def read_json(self, file_path):
        """
        Read a JSON file and return the data.
        :return: dict, the data from the JSON file if read successfully, or return -1 if an error occurs during the reading process.
                    return 0 if the file does not exist.
        """
        # Check if the file exists
        if not os.path.exists(file_path):
            return 0  # Return 0 if the file does not exist
        
        try:
            # Attempt to open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data  # Return the data if read successfully
        except Exception as e:
            # Handle any exceptions that occur during the reading process
            print(f"An error occurred: {e}")
            return -1  # Return -1 if an error occurs

    def write_json(self, data, file_path):
        """
        Write data to a JSON file and save it to the given path.
        :return: 1 if the writing process is successful, or -1, if an error occurs during the writing process.
        """
        try:
            # Attempt to open and write to the JSON file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)  # Write the data to the file with indentation
                return 1  # Return 1 if the writing process is successful
        except Exception as e:
            # Handle any exceptions that occur during the writing process
            print(f"An error occurred: {e}")
            return -1  # Return -1 if an error occurs

    def process_json(self, file_path, remove_key):
        """
        read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.
        :return: 1, if the specified key is successfully removed and the data is written back.
                    0, if the file does not exist or the specified key does not exist in the data.
        
        """
        # Read the JSON file
        data = self.read_json(file_path)
        
        # Check if the file does not exist or an error occurred during reading
        if data == 0 or data == -1:
            return 0  # Return 0 if the file does not exist or an error occurred
        
        # Check if the specified key exists in the data
        if remove_key not in data:
            return 0  # Return 0 if the specified key does not exist
        
        # Remove the specified key from the data
        del data[remove_key]
        
        # Write the modified data back to the file
        result = self.write_json(data, file_path)
        
        # Return 1 if the writing process is successful, otherwise return 0
        return 1 if result == 1 else 0

# Example usage
if __name__ == "__main__":
    processor = JSONProcessor()
    file_path = "example.json"
    remove_key = "key_to_remove"
    
    # Create a sample JSON file
    sample_data = {
        "key1": "value1",
        "key_to_remove": "value2",
        "key3": "value3"
    }
    processor.write_json(sample_data, file_path)
    
    # Process the JSON file
    result = processor.process_json(file_path, remove_key)
    print(f"Result: {result}")