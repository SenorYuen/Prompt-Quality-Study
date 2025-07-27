class ArgumentParser:
    def __init__(self):
        # Initialize the fields: arguments dictionary, types dictionary, and required set
        self.arguments = {}
        self.types = {}
        self.required = set()

    def parse_arguments(self, command_string):
        # Split the command string into a list of arguments
        args = command_string.split()
        
        # Iterate over the arguments in steps of 2 (assuming key-value pairs)
        for i in range(0, len(args), 2):
            # Check if the argument has a corresponding value
            if i + 1 < len(args):
                key = args[i].lstrip('-')  # Remove leading dashes from the key
                value = args[i + 1]
                
                # Check if the key exists in the types dictionary
                if key in self.types:
                    # Convert the value to the specified type
                    self.arguments[key] = self._convert_type(key, value)
                else:
                    # If the key does not exist, add it to the arguments dictionary as a string
                    self.arguments[key] = value
            else:
                # If an argument is missing a value, return False with the missing argument name
                return False, {args[i].lstrip('-')}
        
        # Check for missing required arguments
        missing_args = self.required - set(self.arguments.keys())
        if missing_args:
            return False, missing_args
        else:
            return True, None

    def get_argument(self, key):
        # Retrieve the value of the specified argument from the arguments dictionary
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        # Add the argument to the types dictionary with its corresponding type
        self.types[arg] = arg_type
        
        # If the argument is required, add it to the required set
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        # Try to convert the value to the specified type
        try:
            return self.types[arg](value)
        except (ValueError, TypeError):
            # If the conversion fails, return the original value
            return value