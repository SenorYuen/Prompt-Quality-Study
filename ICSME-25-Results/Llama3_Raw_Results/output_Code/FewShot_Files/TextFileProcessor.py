import json

class TextFileProcessor:
    """
    The class handles reading, writing, and processing text files. It can read the file as JSON, read the raw text, write content to the file, and process the file by removing non-alphabetic characters.
    """

    def __init__(self, file_path):
        """
        Initialize the file path.
        :param file_path: str
        """
        self.file_path = file_path

    # Method to read the file as JSON
    def read_file_as_json(self):
        """
        Read the self.file_path file as json format.
        if the file content doesn't obey json format, the code will raise error.
        :return data: dict if the file is stored as json format, or str/int/float.. according to the file content otherwise.
        """
        try:
            # Attempt to open and read the file as JSON
            with open(self.file_path, 'r') as file:
                # Use json.load to parse the JSON data
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            # If the file is not in JSON format, return None
            return None

    # Method to read the raw text from the file
    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        """
        try:
            # Attempt to open and read the file
            with open(self.file_path, 'r') as file:
                # Use the read method to get the file content
                content = file.read()
                return content
        except FileNotFoundError:
            # If the file does not exist, return None
            return None

    # Method to write content to the file
    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        """
        try:
            # Attempt to open and write to the file
            with open(self.file_path, 'w') as file:
                # Use the write method to write the content
                file.write(str(content))
        except Exception as e:
            # If an error occurs, print the error message
            print(f"An error occurred: {e}")

    # Method to process the file by removing non-alphabetic characters
    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
        """
        try:
            # Attempt to open and read the file
            with open(self.file_path, 'r') as file:
                # Use the read method to get the file content
                content = file.read()
                # Use a list comprehension to filter out non-alphabetic characters
                processed_content = ''.join([char for char in content if char.isalpha()])
                # Attempt to open and write to the file
                with open(self.file_path, 'w') as file:
                    # Use the write method to write the processed content
                    file.write(processed_content)
                return processed_content
        except Exception as e:
            # If an error occurs, print the error message
            print(f"An error occurred: {e}")