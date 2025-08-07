# Prompting Matters: Assessing the Effect of Prompting Techniques on LLM-Generated Class Code

Preprint can be found here: https://aabdllatif.github.io/papers/Adam_ICSME2025.pdf

## Repository Directory:
- In data, you will find the prompts this study uses. 
  - data\ChainOfThought contains our handwritten Chain of Thought prompts 
  - data\ZeroShot contains the Zero Shot prompts. Our pipeline only selects the docstring part of these files. 
  - Few Shot prompts are created dynamically in the pipeline (see below).
- To view the full prompts used by this study, look at the ICSME-25 Results folder.
- In the ICSME-25-Results, you will find the raw output files we used to conduct our analysis. 
  - GPT
    - in ICSME-25-Results\GPT-4o_Raw_Results\output_Code, our different LLM-generated code snippet are sorted by the prompts that were used to generate them. 
    - ICSME-25-Results\GPT-4o_Raw_Results\results.csv is auto-generated to sort all of our data, and the identically named excel file was used to sort the results. 
    - ICSME-25-Results\GPT-4o_Raw_Results\rq1and3Results.xlsx contains the outputs of running the test cases from ClassEval on our LLM generated code, as well as the error analysis we conducted. This contains the data we used for our RQ1 and RQ3 results. 
  - Llama:
    - This directory is far less confusing, and can be found in the ICSME-25-Results\Llama3_Raw_Results. 
- In src, we have the pipeline logic. To run the pipeline, simply run the pipelineOrchestrator file to generate the outputs. They will appear in the results file in a new directory. 


## Environment Setup:

To run the pipeline, you will need a .env file. Configure the .env file like so:
```
GPT_API_KEY = ""
HUGGING_FACE_STARCODER = ""
LLAMA_API_TEMPORARY = ""
```
Ensure that you have the proper number of tokens in your account. 

## Running the Tests

 Follow the instructions below to run the tests.

### Prerequisites

- Python 3.x
- `unittest` module (comes pre-installed with Python)

### Running Tests

To run the tests, use the `run_tests.py` script. This script provides several options to run and manage the tests.

#### Running All Tests

To run all tests in the latest run directory:

```sh
python run_tests.py --all
```

#### Running Tests for a Specific Class

To run tests for a specific class from the latest, use the `--class` option followed by the class name:

```sh
python run_tests.py --class ClassName
```

#### Listing Available Runs and Classes

To list all available valid runs and the classes they contain:

```sh
python run_tests.py --list
```
This also shows errors got when trying to import some classes


#### Reducing Verbosity

To reduce the verbosity of the output, use the `--quiet` option:

```sh
python run_tests.py --quiet
```

### Example Usage

Here are some example commands to run the tests:

```sh
# Run all tests in the latest run directory
python run_tests.py --all

# Run tests for a specific class
python run_tests.py --class JobMarketplace

# List all available valid runs and classes
python run_tests.py --list

# Run tests with reduced verbosity
python run_tests.py --class JobMarketplace --quiet
```

### Notes

- Ensure that the `results` directory contains the output from the runs you want to test.
- The `tests` directory should contain the test files corresponding to the classes in the `output_Code` directories.
