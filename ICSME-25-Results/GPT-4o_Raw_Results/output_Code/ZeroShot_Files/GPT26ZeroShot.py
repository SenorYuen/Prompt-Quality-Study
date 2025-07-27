import csv

class CSVProcessor:

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :return title, data: (list, list), first row is title, the rest is data
        """
        try:
            with open(file_name, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                title = next(reader)  # Read the first row as title
                data = [row for row in reader]  # Read the remaining rows as data
            return title, data
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return [], []

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)  # Write data to the CSV file
            return 1
        except Exception as e:
            print(f"Error writing CSV file: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            title, data = self.read_csv(save_file_name)

            if not title or N >= len(title):
                print("Invalid column index")
                return 0

            # Extract the Nth column and capitalize the data
            processed_data = [[title[N].capitalize()]] + [[row[N].capitalize()] for row in data]

            # Create new file name with '_process' suffix
            new_file_name = save_file_name.replace('.csv', '_process.csv')

            # Write the processed data to the new CSV file
            return self.write_csv(processed_data, new_file_name)
        except Exception as e:
            print(f"Error processing CSV data: {e}")
            return 0