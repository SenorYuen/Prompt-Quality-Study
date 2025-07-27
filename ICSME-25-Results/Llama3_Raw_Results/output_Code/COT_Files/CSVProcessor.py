import csv

class CSVProcessor:
    def __init__(self):
        pass

    def read_csv(self, file_name):
        try:
            with open(file_name, 'r') as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
                if len(data) > 0:
                    title = data[0]
                    data = data[1:]
                    return title, data
                else:
                    return [], []
        except FileNotFoundError:
            return [], []

    def write_csv(self, data, file_name):
        try:
            with open(file_name, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
            return 1
        except Exception as e:
            print(f"Error writing to file: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        title, data = self.read_csv(save_file_name)
        if len(title) > 0 and len(data) > 0:
            new_data = [[row[N].upper()] for row in data]
            new_data.insert(0, [title[N]])
            new_file_name = save_file_name.split('.')[0] + '_process.csv'
            result = self.write_csv(new_data, new_file_name)
            return result
        else:
            return 0