import csv
import json
import os
import re
# Later: Implement Path thing for better practice
from pathlib import Path

def leetcode_CSV_fetcher(path):
    # Extracts the info from the dataset and returns a json formatted output
    results = []

    # Open the input CSV file/dataset
    with open(path, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        
        # Process each row in the input file to a json thing.
        for row in reader:
            # Extract desired information
            row_data = {
                'ID': int(row['ID']),
                'ProblemName': row['Solution'],
                'solution.java': row['Solution.java'],
                'solution.py': row['Solution.py']
            }
            
            # Add the current data to the results array
            dataset_instance = json.dumps(row_data, indent=2)
            results.append(dataset_instance)
    
    return results

def classEval_JSON_fetcher(path):
    # Extracts the info from the dataset and returns a list of dictionaries
    results = []

    # Open the input JSON file
    with open(path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        
        # Process each item in the input file to a dictionary
        for item in data:
            # Convert the entire item to a dictionary and append to results
            item_data = {key: value for key, value in item.items()}
            results.append(item_data)
    
    return results

def get_class_eval_method(parsed_data, problem_id, method_name = None):
    # If method name is provided, fetch the specific method within the class.
    class_id_full = "ClassEval_" + str(problem_id)
    if method_name:
        for item in parsed_data:
            if item['task_id'] == class_id_full:
                for method in item['methods_info']:
                    if method['method_name'] == method_name:
                        return method
        return None
    else:
        # Return the entire class details if method_name is not provided.
        for item in parsed_data:
            if item['task_id'] == class_id_full:
                return item['solution_code']
        return None
    
def get_class_skeleton(parsed_data, class_id):
    # Fetch the skeleton for the specified class.
    for item in parsed_data:
        if item['task_id'] == ('ClassEval_' + str(class_id)):
            return item.get('skeleton', None)
    return None

def get_classname_from_id(parsed_data, class_id):
    for item in parsed_data:
        if item['task_id'] == ('ClassEval_' + str(class_id)):
            return item.get('class_name', None)
    return None



def parse_filename(filename):
    #Parses the filename to extract the number and class name.
    match = re.match(r"(\d+)(.+)\.txt", filename)
    if match:
        number = int(match.group(1))  # Extract the number at the front
        class_name = match.group(2)  # Extract the class name after the number
        return number, class_name
    return None, None

def get_file_content(file_path):
    #Reads the content of a file and returns it as a string.
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def cot_prompt(folder_path):
    # Iterates through all .txt files in a folder, retrieves their content, and stores it in a results list.
    cot_prompts = {}
    a = 0
    for filename in os.listdir(folder_path):
        # if a == 1:
        #     break
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            prompt_to_send = get_file_content(file_path)
            cot_prompts.update({filename: prompt_to_send})
            a += 1
    
    return cot_prompts

def zero_shot_prompt_aggregator(directory):
    extracted_prompts = []

    # Iterate through the Zero Shot directory to grab all the python files. 
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Extract the text between the triple single quotes (docstrings)
                extracted_text = obtain_docstring(content)
                
                # Append the extracted text to the list if it's not empty
                if extracted_text:
                    extracted_prompts.append(extracted_text)
    
    return extracted_prompts

# Takes the docstring from the python file
def obtain_docstring(code):
    pattern = r"'''(.*?)'''"
    match = re.search(pattern, code, re.DOTALL) 
    if match:
        return match.group(1).strip()
    else:
        return ""
