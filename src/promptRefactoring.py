def default_classEval_prompt_handler(parsed_input, prompt_type, input_skeleton, input_class_name, desired_method_details=None):
    system_prompt =  "Provided are instructions for completing the code for a class. Please provide only code with comments in the response."
    instruction = ""
    if prompt_type == "Holistic":
        instruction = "Please complete the class {class_name} in the subsequent code: \n{skeleton}".format(class_name = input_class_name, skeleton = input_skeleton)
    elif prompt_type == "Incremental":
        instruction = "Please complete {method} within the following class {class}. ".format(desired_method_details, )

    # Returns the following items as a tuple.
    return system_prompt, instruction

def few_shot_class_eval_prompt_handler(target_input_skeleton, input_class_name, solution_skeleton, solution_code):
    system_prompt =  "Provided are instructions for completing the code for a class. Please provide only code with comments in the response."
    instruction = "Using the example solution included later, please complete the class {class_name} in the subsequent code: \n{skeleton}. Here is an included question and solution to base a response off of: {skeleton_s}\n\n {code}".format(class_name = input_class_name, skeleton = target_input_skeleton, skeleton_s = solution_skeleton, code = solution_code)
    return system_prompt, instruction
