# Miscelaneous imports
from datetime import datetime
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import HfFolder
#import torch

# Function imports for datasetParsers
from datasetParsers import (classEval_JSON_fetcher, get_class_eval_method, get_class_skeleton, cot_prompt, parse_filename, get_classname_from_id, zero_shot_prompt_aggregator)

# Function imports for promptRefactoring methods
from promptRefactoring import default_classEval_prompt_handler, few_shot_class_eval_prompt_handler

# function imports from outputProcessing
from outputProcessing import (create_data_instance, csv_output, create_python_files_from_csv)

# Function imports for llmPromptingUtilities
from llmPromptingUtilities import (gpt_prompter, huggingFace_prompter, llama_prompter_transofrmer)

from analysis.rq1 import rq1_metrics

if __name__ == "__main__":
    # Use the current time to make a new run directory
    current_time = datetime.now().strftime("run_%Y%m%d_%H%M%S")
    new_dir = os.path.join("results", current_time)
    os.makedirs(new_dir, exist_ok=True)

    # Define where the datasets are in order to access them
    input_csv_path = 'data\\doocs_java_py_human_dataset_file_level.csv'
    input_classEval_path = 'data\\ClassEvalAnalysis\\ClassEval_data.json'
    input_classEval_path_zeroShot = 'data\\ZeroShot\\benchmark_solution_code'
    output_csv_path = os.path.join(new_dir, "results.csv")

    # Get parsable data from said locations
    classEval_input_aggregate = classEval_JSON_fetcher(input_classEval_path)
    classEval_zero_shot_aggregate = zero_shot_prompt_aggregator(input_classEval_path_zeroShot)
    # leetcode_input_aggregate = leetcode_CSV_fetcher(input_csv_path)
    
    # Instantiating data array for later, and define what LLMS should be used
    results = []
    llm_labels = ["GPT"]

    # Setup Llama transformer model if necessary
    if "Llama" in llm_labels:
        api_token = "put something here"
        HfFolder.save_token(api_token)

        # Load models and tokenizers (models/tokenizers are from huggingface)
        model_info = {
            'Llama3': {
                'tokenizer': 'meta-llama/Meta-Llama-3-8B-Instruct',
                'model': 'meta-llama/Meta-Llama-3-8B-Instruct',
                'model_class': AutoModelForCausalLM
            }
        }

        # Load the Llama3 model and tokenizer
        model_name = 'Llama3'
        info = model_info[model_name]
        try:
            tokenizer = AutoTokenizer.from_pretrained(info['tokenizer'])
            model = info['model_class'].from_pretrained(info['model'])
        except Exception as e:
            print(f"Error loading model {model_name}: {e}")
    
    # COT Zero Shot Prompt Logic
    cot_prompt_dict = cot_prompt("data\\ChainOfThought")
    system_prompt = "Provided are instructions for completing the code for a class. Please provide the only code in your response."
    for llm in llm_labels:
        for key in cot_prompt_dict:
            # Retrieve the whole prompt from the text file in the directory.
            filename_info = parse_filename(key)
            task_id = filename_info[0]
            original_code = get_class_eval_method(classEval_input_aggregate, filename_info[0])
            
            if llm == "GPT":
                prompt_output = gpt_prompter(
                    system_prompt,
                    cot_prompt_dict[key]
                )
                print(prompt_output)
                create_data_instance(results, "GPT", task_id, original_code, "COT", prompt_output)
            if llm == "Llama":
                prompt_output = llama_prompter_transofrmer(
                    model,
                    tokenizer,
                    cot_prompt_dict[key]
                )
                create_data_instance(results, "Llama", task_id, original_code, "COT", prompt_output)
            if llm == "StarCoder":
                prompt_output = huggingFace_prompter("StarCoder", cot_prompt_dict[key]) 
                create_data_instance(results, "StarCoder", task_id, original_code, "COT", prompt_output)
    print("COT done")

    prompt_version = "COTFewShot"
    for llm in llm_labels:
        for key in cot_prompt_dict:
            filename_info = parse_filename(key)
            task_id = filename_info[0]
            original_code = get_class_eval_method(classEval_input_aggregate, filename_info[0])

            # Include an example in the prompt - always is Task 99
            reference_solution_code = get_class_eval_method(classEval_input_aggregate, 99)
            reference_cot_prompt = cot_prompt_dict["99ZipFileProcessor.txt"]
            prompt_body = cot_prompt_dict[key] + "\n Use the following prompt and solution pair as context for generating the previously mentioned class: \n" + reference_cot_prompt + "\n" + reference_solution_code
            
            if llm == "GPT":
                prompt_output = gpt_prompter(system_prompt, prompt_body)
                create_data_instance(results, "GPT", task_id, original_code, prompt_version, prompt_output)
                print(prompt_output)
            if llm == "StarCoder":
                prompt_output = huggingFace_prompter("StarCoder", prompt_body)
                create_data_instance(results, "StarCoder", task_id, original_code, prompt_version, prompt_output)
            if llm == "Llama":
                prompt_output = prompt_output = llama_prompter_transofrmer(
                    model,
                    tokenizer,
                    cot_prompt_dict[key]
                )
                create_data_instance(results, "Llama", task_id, original_code, prompt_version, prompt_output)
    print("COT Few Shot done")

    # Basic Class Eval Holistic Generation prompt logic
    prompt_version = "ZeroShot"
    for llm in llm_labels:
        for sample_class_id in range(0, 99): # Omit last one for few shot

            # Construct the prompt by getting necessary information.
            class_name = get_classname_from_id(classEval_input_aggregate, sample_class_id)
            solution_code = get_class_eval_method(classEval_input_aggregate, sample_class_id)
            skeleton = classEval_zero_shot_aggregate[sample_class_id]
            sample_prompt = default_classEval_prompt_handler(classEval_input_aggregate, "Holistic", skeleton, class_name)

            # Sending the prompt to ChatGPT
            # sample_prompt[1] is system prompt, sample_prompt[0] is the full instruction w/ class skeleton
            if llm == "GPT":
                prompt_output = gpt_prompter(sample_prompt[1], sample_prompt[0])
                create_data_instance(results, llm, sample_class_id, solution_code, prompt_version, prompt_output)
                print(prompt_output)
            if llm == "StarCoder":
                prompt_output = huggingFace_prompter("StarCoder", sample_prompt[0])
                create_data_instance(results, llm, sample_class_id, solution_code, prompt_version, prompt_output)
            if llm == "Llama":
                prompt_output = prompt_output = llama_prompter_transofrmer(
                    model,
                    tokenizer,
                    sample_prompt[0]
                )
                create_data_instance(results, llm, sample_class_id, solution_code, prompt_version, prompt_output)
    print("Basic CE done")


    prompt_version = "FewShot"
    for llm in llm_labels:
        for sample_class_id in range(0, 99):
            # Get necessary information for the target question
            class_name = get_classname_from_id(classEval_input_aggregate, sample_class_id)
            solution_code = get_class_eval_method(classEval_input_aggregate, sample_class_id)
            skeleton = get_class_skeleton(classEval_input_aggregate, sample_class_id)

            # Get necessary information for the context question (solution code) - hardcoded to one example
            example_class_name = get_classname_from_id(classEval_input_aggregate, 98)
            example_skeleton = get_class_skeleton(classEval_input_aggregate, 98)
            example_solution = get_class_eval_method(classEval_input_aggregate, 98)

            # Construct the prompt
            sample_prompt = few_shot_class_eval_prompt_handler(skeleton, class_name, example_skeleton, example_solution)
            
            if llm == "GPT":
                prompt_output = gpt_prompter(sample_prompt[1], sample_prompt[0])
                create_data_instance(results, llm, sample_class_id, solution_code, prompt_version, prompt_output)
                print(prompt_output)
            if llm == "StarCoder":
                prompt_output = huggingFace_prompter("StarCoder", sample_prompt[0])
                create_data_instance(results, llm, sample_class_id, solution_code, prompt_version, prompt_output)
            if llm == "Llama":
                prompt_output = prompt_output = llama_prompter_transofrmer(
                    model,
                    tokenizer,
                    sample_prompt[0]
                )
                create_data_instance(results, llm, sample_class_id, solution_code, prompt_version, prompt_output)
    print("Few shot CE done")


    #Parse all data into a CSV
    csv_output(output_csv_path, results)

    # Compute BLEU3 and ROUGE metrics
    rq1_metrics(output_csv_path)

    # Put all generated code into individual python files.
    python_output_directory = os.path.join(new_dir, "output_Code")
    os.makedirs(python_output_directory, exist_ok=True)
    create_python_files_from_csv(output_csv_path, python_output_directory)