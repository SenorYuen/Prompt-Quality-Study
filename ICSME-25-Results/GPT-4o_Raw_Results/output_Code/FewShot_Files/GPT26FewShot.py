import csv

class CSVProcessor:
    """
    This is a class for processing CSV files, including reading and writing CSV data,
    as well as processing specific operations and saving as a new CSV file.
    """

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        """
        try:
            with open(file_name, mode='r', newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                # Read the first row as title
                title = next(csvreader)
                # Read the rest as data
                data = [row for row in csvreader]
            return title, data
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None, None

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return: int, if success return 1, or 0 otherwise
        """
        try:
            with open(file_name, mode='w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                # Write each row in data to the CSV file
                csvwriter.writerows(data)
            return 1
        except Exception as e:
            print(f"Error writing CSV file: {e}")
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the Nth (from 0) column data and capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the Nth column(from 0)
        :param save_file_name: the name of file that needs to be processed.
        :return: int, if success return 1, or 0 otherwise
        """
        try:
            # Read the original CSV file
            title, data = self.read_csv(save_file_name)
            if not title or not data:
                return 0
            
            # Capitalize the Nth column data
            new_data = [[row[N].upper()] for row in data]

            # Create new file name with '_process' suffix
            new_file_name = save_file_name.replace('.csv', '_process.csv')

            # Write the processed data to the new CSV file
            self.write_csv([title] + new_data, new_file_name)
            return 1
        except Exception as e:
            print(f"Error processing CSV data: {e}")
            return 0