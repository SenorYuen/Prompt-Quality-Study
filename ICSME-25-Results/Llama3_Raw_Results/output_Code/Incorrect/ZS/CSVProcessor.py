import csv

class CSVProcessor:

    def __init__(self, file_name=None):
        # Initialize the class with a file name if provided
        self.file_name = file_name

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :return title, data: (list, list), first row is title, the rest is data
        """
        try:
            with open(file_name, 'r') as file:
                # Use csv.reader to read the csv file
                csv_reader = csv.reader(file)
                # Get the title (first row) and data
                title = next(csv_reader)
                data = list(csv_reader)
                return title, data
        except FileNotFoundError:
            # Handle the case when the file does not exist
            print(f"File {file_name} not found.")
            return None, None

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :return:int, if success return 1, or 0 otherwise
        """
        try:
            with open(file_name, 'w', newline='') as file:
                # Use csv.writer to write the csv file
                csv_writer = csv.writer(file)
                # Write the data to the csv file
                csv_writer.writerows(data)
                return 1
        except Exception as e:
            # Handle any exceptions during writing
            print(f"Error writing to file {file_name}: {str(e)}")
            return 0

    def process_csv_data(self, N, save_file_name=None):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :return:int, if success return 1, or 0 otherwise
        """
        if self.file_name is None:
            # If no file name is provided, return an error
            print("No file name provided.")
            return 0
        
        # Read the csv file
        title, data = self.read_csv(self.file_name)
        
        if title is None or data is None:
            # If reading the csv file fails, return an error
            return 0
        
        # Process the data
        new_title = [title[N].upper()]
        new_data = [[row[N].upper()] for row in data]
        
        # If save_file_name is not provided, generate a new file name
        if save_file_name is None:
            save_file_name = self.file_name.split('.')[0] + '_process.csv'
        
        # Write the new data to a csv file
        new_data.insert(0, new_title)
        return self.write_csv(new_data, save_file_name)


# Example usage
if __name__ == "__main__":
    processor = CSVProcessor('example.csv')
    processor.process_csv_data(1)