import openpyxl

class ExcelProcessor:
    """
    This is a class for processing excel files, including reading and writing excel data, as well as processing specific operations and saving as a new excel file.
    """

    def __init__(self):
        # Initialize an empty ExcelProcessor object
        pass

    def read_excel(self, file_name):
        """
        Reading data from Excel files
        :param file_name: str, Excel file name to read
        :return: list of data, Data in Excel
        """
        try:
            # Load the Excel file
            wb = openpyxl.load_workbook(file_name)
            # Select the first sheet
            sheet = wb.active
            # Initialize an empty list to store data
            data = []
            # Iterate over each row in the sheet
            for row in sheet.rows:
                # Initialize an empty list to store row data
                row_data = []
                # Iterate over each cell in the row
                for cell in row:
                    # Append the cell value to the row data
                    row_data.append(cell.value)
                # Append the row data to the data list
                data.append(tuple(row_data))
            # Return the data list
            return data
        except:
            # Return None if an error occurs
            return None

    def write_excel(self, data, file_name):
        """
        Write data to the specified Excel file
        :param data: list, Data to be written
        :param file_name: str, Excel file name to write to
        :return: 0 or 1, 1 represents successful writing, 0 represents failed writing
        """
        try:
            # Create a new Excel file
            wb = openpyxl.Workbook()
            # Select the first sheet
            sheet = wb.active
            # Iterate over each row in the data
            for row in data:
                # Write the row to the sheet
                sheet.append(row)
            # Save the Excel file
            wb.save(file_name)
            # Return 1 to indicate successful writing
            return 1
        except:
            # Return 0 to indicate failed writing
            return 0

    def process_excel_data(self, N, save_file_name):
        """
        Change the specified column in the Excel file to uppercase
        :param N: int, The serial number of the column that want to change
        :param save_file_name: str, source file name
        :return: (int, str), The former is the return value of write_excel, while the latter is the saved file name of the processed data
        """
        try:
            # Read the Excel file
            data = self.read_excel(save_file_name)
            # Check if data is not None
            if data is not None:
                # Initialize an empty list to store processed data
                processed_data = []
                # Iterate over each row in the data
                for row in data:
                    # Initialize an empty list to store row data
                    row_data = list(row)
                    # Check if the column index is within the row bounds
                    if N <= len(row):
                        # Convert the column value to uppercase
                        row_data[N-1] = str(row_data[N-1]).upper()
                    # Append the row data to the processed data
                    processed_data.append(tuple(row_data))
                # Write the processed data to a new Excel file
                success = self.write_excel(processed_data, 'processed_' + save_file_name)
                # Return the success value and the saved file name
                return success, 'processed_' + save_file_name
            else:
                # Return 0 and None if data is None
                return 0, None
        except:
            # Return 0 and None if an error occurs
            return 0, None