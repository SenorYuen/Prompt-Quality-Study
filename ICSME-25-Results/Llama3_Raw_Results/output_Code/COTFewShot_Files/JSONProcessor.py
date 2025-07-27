import json
import os


class JSONProcessor:
    def __init__(self):
        pass

    def read_json(self, file_path):
        try:
            if not os.path.exists(file_path):
                return 0
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except:
            return -1

    def write_json(self, data, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file)
            return 1
        except:
            return -1

    def process_json(self, file_path, remove_key):
        try:
            if not os.path.exists(file_path):
                return 0
            with open(file_path, 'r') as file:
                data = json.load(file)
            if remove_key in data:
                del data[remove_key]
                with open(file_path, 'w') as file:
                    json.dump(data, file)
                return 1
            else:
                return 0
        except:
            return 0