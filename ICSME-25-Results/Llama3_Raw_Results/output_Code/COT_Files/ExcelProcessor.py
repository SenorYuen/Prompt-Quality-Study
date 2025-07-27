import openpyxl

class ExcelProcessor:
    def __init__(self):
        pass

    def read_excel(self, file_name):
        try:
            wb = openpyxl.load_workbook(file_name)
            sheet = wb.active
            data = []
            for row in sheet.rows:
                row_data = []
                for cell in row:
                    row_data.append(cell.value)
                data.append(tuple(row_data))
            return data
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

    def write_excel(self, data, file_name):
        try:
            wb = openpyxl.Workbook()
            sheet = wb.active
            for row in data:
                sheet.append(row)
            wb.save(file_name)
            return 1
        except Exception as e:
            print(f"Error writing Excel file: {e}")
            return 0

    def process_excel_data(self, N, save_file_name):
        data = self.read_excel(save_file_name)
        if data is None:
            return 0, None
        processed_data = []
        for row in data:
            processed_row = list(row)
            if N <= len(processed_row):
                processed_row[N-1] = str(processed_row[N-1]).upper()
            processed_data.append(tuple(processed_row))
        write_result = self.write_excel(processed_data, 'processed_' + save_file_name)
        return write_result, 'processed_' + save_file_name