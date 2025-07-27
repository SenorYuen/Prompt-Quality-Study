import zipfile
import os

class ZipFileProcessor:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_zip_file(self):
        try:
            return zipfile.ZipFile(self.file_name, 'r')
        except FileNotFoundError:
            return None

    def extract_all(self, output_path):
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extractall(output_path)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def extract_file(self, file_name, output_path):
        try:
            with zipfile.ZipFile(self.file_name, 'r') as zip_ref:
                zip_ref.extract(file_name, output_path)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def create_zip_file(self, files, output_file_name):
        try:
            with zipfile.ZipFile(output_file_name, 'w') as zip_ref:
                for file in files:
                    if os.path.isfile(file):
                        zip_ref.write(file, os.path.basename(file))
                    else:
                        print(f"{file} is not a valid file.")
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False