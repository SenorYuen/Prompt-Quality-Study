class ArgumentParser:
    def __init__(self):
        """
        Initialize the fields.
        """
        # Dictionary to store argument types
        self.types = {}
        # Set to store required arguments
        self.required = set()
        # Dictionary to store parsed arguments and their values
        self.arguments = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and stores the parsed result in specific type 
        in the arguments dictionary. Checks for missing required arguments, if any, and returns False 
        with the missing argument names, otherwise returns True.
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        """
        # Split the command string into arguments
        tokens = command_string.split()
        
        # Iterate over tokens and parse them
        for token in tokens:
            if token.startswith('--'):
                key = token[2:]
                # Attempt to get the value associated with the key
                value_index = tokens.index(token) + 1
                if value_index < len(tokens):
                    value = tokens[value_index]
                    # Convert the value to the appropriate type
                    self.arguments[key] = self._convert_type(key, value)
        
        # Check for missing required arguments
        missing_args = self.required - self.arguments.keys()
        if missing_args:
            return False, missing_args
        return True, None

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :return: The value of the argument, or None if the argument does not exist.
        """
        return self.arguments.get(key, None)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it will be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        """
        # Store the type of the argument
        self.types[arg] = arg_type
        # If the argument is required, add it to the required set
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :return: return corresponding value in self.types if convert successfully, or the input value otherwise
        """
        # Get the type for the argument
        arg_type = self.types.get(arg, str)
        try:
            # Convert the value to the specified type
            return arg_type(value)
        except ValueError:
            # Return the original value if conversion fails
            return value