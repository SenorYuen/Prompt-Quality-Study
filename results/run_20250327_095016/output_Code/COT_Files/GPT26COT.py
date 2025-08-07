import csv

class CSVProcessor:
    def __init__(self):
        pass

    def read_csv(self, file_name):
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
            title = data[0]
            data = data[1:]
        return title, data

    def write_csv(self, data, file_name):
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except Exception as e:
            return 0

    def process_csv_data(self, N, save_file_name):
        try:
            title, data = self.read_csv(save_file_name)
            new_data = [[row[N].upper()] for row in data]
            new_file_name = save_file_name.replace('.csv', '_process.csv')
            self.write_csv([title] + new_data, new_file_name)
            return 1
        except Exception as e:
            return 0