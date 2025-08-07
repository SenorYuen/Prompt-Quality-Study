# Miscelaneous imports
from datetime import datetime
import os

# Function imports for datasetParsers
from datasetParsers import (classEval_JSON_fetcher, get_class_eval_method, get_class_skeleton, cot_prompt, parse_filename, get_classname_from_id)

# Function imports for promptRefactoring methods
from promptRefactoring import default_classEval_prompt_handler, few_shot_class_eval_prompt_handler

# function imports from outputProcessing
from outputProcessing import (create_data_instance, csv_output, create_python_files_from_csv)

# Function imports for llmPromptingUtilities
from llmPromptingUtilities import gpt_prompter
from llmPromptingUtilities import huggingFace_prompter

import requests
def query(payload):
    starcoder_api_key = os.getenv('HUGGING_FACE_STARCODER')
    STARCODER_API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
    headers = {"Authorization": f"Bearer {starcoder_api_key}"}
    response = requests.post(STARCODER_API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
    try:
        # Check if the response is a list
        response_json = response.json()
        
        if isinstance(response_json, list):
            # Assuming we want the first item in the list
            return response_json[0].get("generated_text", "No generated text")
        else:
            # Handle single response (not in a list)
            return response_json.get("generated_text", "No generated text")
    
    except ValueError:
        print("Response did not contain valid JSON:", response.text)
        return None

def starCoder_prompter(promptText):
    # Properly formatted payload
    formattedPromptInput = {
        "inputs": promptText,
        "parameters": {
            "max_new_tokens": 1000,  # Adjust as necessary
            "return_full_text_": False
        }
    }
    return query(formattedPromptInput)

system_prompt = "Provided are instructions for completing the code for a class. Please provide only code in the response."
cot_prompt_dict = cot_prompt("data\\ChainOfThought")
for key in cot_prompt_dict:
    print(huggingFace_prompter("Llama", cot_prompt_dict[key]))
    break

