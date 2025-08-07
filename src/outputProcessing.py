import csv
import os
import pandas as pd
import re

def csv_output(path, data):
    fieldnames = ['Question Source', 'Question ID', 'Original Code', 'Prompt Version', 'Output Code']
    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the column headers
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def create_data_instance(data_array, q_source, q_id, original_code, prompt_version, output):
    data_instance = {
        'Question Source': q_source,
        'Question ID': q_id,
        'Original Code': original_code,
        'Prompt Version': prompt_version,
        'Output Code': output
    }
    data_array.append(data_instance)
    return data_array

def create_python_files_from_csv(csv_file_path, output_directory):
    data = pd.read_csv(csv_file_path)
    os.makedirs(output_directory, exist_ok=True)

    # Iterate through each row in the DataFrame
    for index, row in data.iterrows():
        # Construct the filename using the specified columns
        file_name = f"{row['Question Source']}{row['Question ID']}{row['Prompt Version']}.py"
        file_path = os.path.join(output_directory, file_name)

        # Remove GPT formatting if necessary
        original_code = row['Output Code']
        match = re.search(r'```python(.*?)```', original_code, re.DOTALL)
        if match:
            original_code = match.group(1).strip()

        # Write the content of the 'Original Code' column to the Python file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(original_code)

        print(f"Created {file_name} with content from row {index + 1}.")