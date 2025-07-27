import csv

class CSVProcessor:
    def __init__(self):
        pass

    def read_csv(self, file_name):
        try:
            with open(file_name, 'r') as file:
                csv_reader = csv.reader(file)
                title = next(csv_reader)
                data = list(csv_reader)
            return title, data
        except:
            return None

    def write_csv(self, data, file_name):
        try:
            with open(file_name, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
            return 1
        except:
            return 0

    def process_csv_data(self, N, save_file_name):
        try:
            title, data = self.read_csv(save_file_name)
            new_data = [[row[N].upper()] for row in data]
            new_title = [title[N]]
            new_file_name = save_file_name.split('.')[0] + '_process.csv'
            self.write_csv([new_title] + new_data, new_file_name)
            return 1
        except:
            return 0