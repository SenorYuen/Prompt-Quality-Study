import csv

class CSVProcessor:
    def __init__(self):
        pass

    def read_csv(self, file_name):
        try:
            with open(file_name, mode='r', newline='') as file:
                csv_reader = csv.reader(file)
                title = next(csv_reader)
                data = [row for row in csv_reader]
            return title, data
        except:
            return None, None

    def write_csv(self, data, file_name):
        try:
            with open(file_name, mode='w', newline='') as file:
                csv_writer = csv.writer(file)
                for row in data:
                    csv_writer.writerow(row)
            return 1
        except:
            return 0

    def process_csv_data(self, N, save_file_name):
        try:
            title, data = self.read_csv(save_file_name)
            if title is None or data is None:
                return 0

            new_data = [[row[N].upper()] for row in data]
            new_file_name = save_file_name.replace('.csv', '_process.csv')
            self.write_csv([title] + new_data, new_file_name)
            return 1
        except:
            return 0