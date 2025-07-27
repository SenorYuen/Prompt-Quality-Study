class ArgumentParser:
    """
    This is a class for parsing command line arguments to a dictionary.
    """

    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.required is a set that stores the required arguments
        self.types is a dict that stores type of every argument.
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails
        """
        # Split the command string into individual arguments
        args = command_string.split()

        # Iterate over the arguments
        for arg in args:
            if arg.startswith('--'):
                # Handle arguments like --arg=value
                key, value = arg[2:].split('=')
                self.arguments[key] = self._convert_type(key, value)
            elif arg.startswith('-'):
                # Handle options like -option
                key = arg[1:]
                self.arguments[key] = True

        # Check for missing required arguments
        missing_args = self.required - self.arguments.keys()
        if missing_args:
            return False, missing_args
        return True, None

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        """
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type: type, Argument type, default is str
        """
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param arg: str, argument name
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value otherwise
        """
        arg_type = self.types.get(arg, str)
        try:
            return arg_type(value)
        except ValueError:
            return value