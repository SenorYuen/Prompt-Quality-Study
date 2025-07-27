import json
import os

class JSONProcessor:
    def read_json(self, file_path: str) -> dict:
        """
        Reads a JSON file and returns the data.
        
        Args:
        file_path (str): The path of the JSON file.
        
        Returns:
        dict: The data from the JSON file if read successfully, -1 if an error occurs during the reading process, 0 if the file does not exist.
        """
        try:
            # Check if the file exists
            if not os.path.exists(file_path):
                return 0
            
            # Open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        
        except json.JSONDecodeError:
            # Return -1 if an error occurs during the reading process
            return -1
    
    def write_json(self, data: dict, file_path: str) -> int:
        """
        Writes data to a JSON file and saves it to the given path.
        
        Args:
        data (dict): The data to be written to the JSON file.
        file_path (str): The path of the JSON file.
        
        Returns:
        int: 1 if the writing process is successful, -1 if an error occurs during the writing process.
        """
        try:
            # Open and write the JSON file
            with open(file_path, 'w') as file:
                json.dump(data, file)
                return 1
        
        except Exception as e:
            # Return -1 if an error occurs during the writing process
            print(f"An error occurred: {e}")
            return -1
    
    def process_json(self, file_path: str, remove_key: str) -> int:
        """
        Reads a JSON file, removes a specified key, and rewrites the modified data back to the file.
        
        Args:
        file_path (str): The path of the JSON file.
        remove_key (str): The key to be removed.
        
        Returns:
        int: 1 if the specified key is successfully removed and the data is written back, 0 if the file does not exist or the specified key does not exist in the data.
        """
        # Read the JSON file
        data = self.read_json(file_path)
        
        # Check if the file exists and the data is not empty
        if data == 0 or data == -1:
            return 0
        
        # Check if the key exists in the data
        if remove_key not in data:
            return 0
        
        # Remove the key from the data
        del data[remove_key]
        
        # Write the modified data back to the file
        result = self.write_json(data, file_path)
        
        # Return 1 if the writing process is successful
        if result == 1:
            return 1
        else:
            return 0