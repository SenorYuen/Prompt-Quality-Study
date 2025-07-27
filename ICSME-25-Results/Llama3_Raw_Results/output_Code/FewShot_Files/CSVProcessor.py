import csv

class CSVProcessor:
    """
    This is a class for processing CSV files, including reading and writing CSV data, as well as processing specific operations and saving as a new CSV file.
    """

    def __init__(self):
        # Initialize the CSVProcessor object
        pass

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :param file_name: str, name of the csv file
        :return title, data: (list, list), first row is title, the rest is data
        """
        try:
            # Open the CSV file in read mode
            with open(file_name, 'r') as file:
                # Create a CSV reader object
                csv_reader = csv.reader(file)
                # Read the title (first row)
                title = next(csv_reader)
                # Read the data (rest of the rows)
                data = list(csv_reader)
                # Return the title and data
                return title, data
        except FileNotFoundError:
            # Handle the case when the file is not found
            print(f"File '{file_name}' not found.")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :param file_name: str, name of the csv file
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            # Open the CSV file in write mode
            with open(file_name, 'w', newline='') as file:
                # Create a CSV writer object
                csv_writer = csv.writer(file)
                # Write the data to the CSV file
                csv_writer.writerows(data)
                # Return success (1)
                return 1
        except Exception as e:
            # Handle any exceptions
            print(f"An error occurred: {e}")
            # Return failure (0)
            return 0

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :param N: int, the N th column(from 0)
        :param save_file_name, the name of file that needs to be processed.
        :return:int, if success return 1, or 0 otherwise
        """
        # Read the CSV file
        title, data = self.read_csv(save_file_name)
        if title is None or data is None:
            # If reading the file failed, return failure (0)
            return 0
        # Process the data (capitalize the Nth column)
        new_data = [[row[N].upper()] for row in data]
        # Create the new title (only the Nth column)
        new_title = [title[N]]
        # Create the new CSV data
        new_csv_data = [new_title] + new_data
        # Create the new file name by adding '_process' to the original file name
        new_file_name = save_file_name.split('.')[0] + '_process.csv'
        # Write the new CSV data to the new file
        return self.write_csv(new_csv_data, new_file_name)