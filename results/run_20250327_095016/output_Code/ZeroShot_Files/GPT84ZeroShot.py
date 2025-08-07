import json

class TextFileProcessor:
    def __init__(self, file_path):
        """
        Initialize the file path.
        """
        self.file_path = file_path

    def read_file_as_json(self):
        """
        Read the self.file_path file as json format.
        if the file content doesn't obey json format, the code will raise error.
        :return data: dict if the file is stored as json format, or str/int/float.. according to the file content otherwise.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
        """
        content = self.read_file()
        # Filter out non-alphabetic characters
        processed_content = ''.join(filter(str.isalpha, content))
        # Write the processed content back to the file
        self.write_file(processed_content)