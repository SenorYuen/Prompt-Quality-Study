class ArgumentParser:
    """
    This is a class for parsing command line arguments to a dictionary.
    """

    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.requried is a set that stores the required arguments
        self.types is a dict that stores type of every arguments.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        # Split the command string into parts
        parts = command_string.split()
        
        # Initialize index to track current part
        i = 1
        
        # Iterate over each part
        while i < len(parts):
            # Check if part is an option
            if parts[i].startswith('-'):
                # Check if option has a value
                if '=' in parts[i]:
                    # Split option and value
                    arg, value = parts[i][2:].split('=')
                    # Store argument and value in dictionary
                    self.arguments[arg] = self._convert_type(arg, value)
                # Check if option is a flag
                elif i + 1 < len(parts) and not parts[i + 1].startswith('-'):
                    # Store argument and value in dictionary
                    arg = parts[i][1:]
                    self.arguments[arg] = self._convert_type(arg, parts[i + 1])
                    # Increment index to skip value
                    i += 1
                # If option is a flag with no value
                else:
                    # Store argument and value in dictionary
                    arg = parts[i][1:]
                    self.arguments[arg] = True
            # Increment index
            i += 1
        
        # Check for missing required arguments
        missing_args = self.required - set(self.arguments.keys())
        
        # Return result
        if missing_args:
            return False, missing_args
        else:
            return True, None

    def get_argument(self, key):
        # Return value of argument from dictionary
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        # Store argument type in dictionary
        self.types[arg] = arg_type
        
        # If argument is required, add to set
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        # Get type of argument from dictionary
        arg_type = self.types.get(arg)
        
        # Try to convert value to type
        if arg_type == int:
            try:
                return int(value)
            except ValueError:
                pass
        elif arg_type == float:
            try:
                return float(value)
            except ValueError:
                pass
        elif arg_type == bool:
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
        
        # If conversion fails, return original value
        return value