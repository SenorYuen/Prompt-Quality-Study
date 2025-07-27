class ArgumentParser:
    def __init__(self):
        # Initialize the fields
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        # Split the command string into parts
        parts = command_string.split()
        
        # Initialize an index to track the current part
        i = 1
        
        # Iterate over the parts
        while i < len(parts):
            # Check if the part is an argument
            if parts[i].startswith('-'):
                # Extract the argument name
                arg_name = parts[i].lstrip('-')
                
                # Check if the argument has a value
                if '=' in arg_name:
                    # Split the argument name and value
                    arg_name, value = arg_name.split('=')
                elif i + 1 < len(parts) and not parts[i + 1].startswith('-'):
                    # The value is the next part
                    value = parts[i + 1]
                    i += 1
                else:
                    # The argument is a flag
                    value = True
                # Convert the value to the specified type
                value = self._convert_type(arg_name, value)
                
                # Add the argument to the arguments dictionary
                self.arguments[arg_name] = value
            i += 1
        
        # Check for missing required arguments
        missing_args = self.required - set(self.arguments.keys())
        
        # Return the result
        if missing_args:
            return False, missing_args
        else:
            return True, None

    def get_argument(self, key):
        # Return the value of the argument
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        # Add the argument to the types dictionary
        self.types[arg] = arg_type
        
        # Add the argument to the required set if it is required
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        # Get the type of the argument
        arg_type = self.types.get(arg)
        
        # Try to convert the value to the specified type
        if arg_type == int:
            try:
                return int(value)
            except ValueError:
                pass
        elif arg_type == bool:
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
        # If the conversion fails, return the original value
        return value