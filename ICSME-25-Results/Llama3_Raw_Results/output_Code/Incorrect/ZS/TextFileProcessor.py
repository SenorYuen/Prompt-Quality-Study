import json

class TextFileProcessor:
    # Initialize the file path
    def __init__(self, file_path):
        self.file_path = file_path  # Store the file path as an instance variable

    # Read the file as JSON
    def read_file_as_json(self):
        try:
            # Attempt to open and read the file as JSON
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError:
            # If the file is not in JSON format, raise an error
            raise ValueError("The file is not in JSON format")

    # Read the file
    def read_file(self):
        # Open and read the file
        with open(self.file_path, 'r') as file:
            return file.read()

    # Write content to the file
    def write_file(self, content):
        # Open and write to the file, overwriting any existing content
        with open(self.file_path, 'w') as file:
            file.write(str(content))

    # Process the file by removing non-alphabetic characters
    def process_file(self):
        # Read the file content
        content = self.read_file()
        
        # Filter out non-alphabetic characters
        processed_content = ''.join(filter(str.isalpha, content))
        
        # Overwrite the processed content to the file
        self.write_file(processed_content)