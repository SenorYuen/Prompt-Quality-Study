class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        args = command_string.split()
        missing_args = set(self.required)
        for arg in args:
            if arg.startswith('--'):
                key, value = arg[2:].split('=')
                self.arguments[key] = self._convert_type(key, value)
                missing_args.discard(key)
            elif arg.startswith('-'):
                key = arg[1:]
                self.arguments[key] = True
                missing_args.discard(key)
        
        if missing_args:
            return False, missing_args
        return True, None

    def get_argument(self, key):
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        try:
            return self.types[arg](value)
        except (ValueError, KeyError):
            return value