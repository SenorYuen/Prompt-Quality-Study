import json

class TextFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_as_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse JSON: {e}")

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise Exception(f"File '{self.file_path}' not found")

    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(str(content))

    def process_file(self):
        try:
            content = self.read_file()
            processed_content = ''.join(filter(str.isalpha, content))
            self.write_file(processed_content)
            return processed_content
        except Exception as e:
            raise Exception(f"Failed to process file: {e}")