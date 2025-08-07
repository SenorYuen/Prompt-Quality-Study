import openai
import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import HfFolder
#import torch

load_dotenv()

openai.api_key = os.getenv('GPT_API_KEY')

def gpt_prompter(full_prompt, system_prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5
        )
        prompt_output = response.choices[0].message['content'].strip()
        return prompt_output
    except Exception as e:
        print(f"Error: {e}")
        return None
    


# from llamaapi import LlamaAPI
# import json

# llama = LlamaAPI(os.getenv('LLAMA_API_TEMPORARY'))

# def llama_prompter(prompt_input, prompt_content):
#     api_request_json = {
#     "model": "llama3-70b",
#     "max_tokens": 1000,
#     "messages": [
#         {"role": "system", "content": prompt_content},
#         {"role": "user", "content": prompt_input},
#     ]
#     }

#     # Make your request and handle the response
#     response = llama.run(api_request_json)
#     print(json.dumps(response.json(), indent=2))

import requests
def starCoder_query(payload):
    starcoder_api_key = os.getenv('HUGGING_FACE_STARCODER')
    API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"
    headers = {"Authorization": f"Bearer {starcoder_api_key}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    
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

def llama_query(payload):
    llama_api_key = os.getenv('HUGGING_FACE_STARCODER')
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B"
    headers = {"Authorization": f"Bearer {llama_api_key}"}
    response = requests.post(API_URL, headers=headers, json=payload)
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
    

def huggingFace_prompter(llm, promptText):
    # Properly formatted payload
    formattedPromptInput = {
        "inputs": promptText,
        "parameters": {
            "max_new_tokens": 1000,  # Adjust as necessary
            "return_full_text_": False
        }
    }
    if llm == "StarCoder":
        return starCoder_query(formattedPromptInput)
    if llm == "Llama":
        return llama_query(formattedPromptInput)


# Function to get model output
def llama_prompter_transofrmer(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]
    if input_ids.max() >= model.config.vocab_size:
        raise ValueError(f"Token ID {input_ids.max()} is out of the valid range for the model's vocabulary size {model.config.vocab_size}")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=1000)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)