class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        args = command_string.split()
        i = 0
        while i < len(args):
            if args[i].startswith('--'):
                arg_name = args[i][2:]
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    arg_value = args[i + 1]
                    i += 2
                else:
                    arg_value = True
                    i += 1
            elif args[i].startswith('-'):
                arg_name = args[i][1:]
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    arg_value = args[i + 1]
                    i += 2
                else:
                    arg_value = True
                    i += 1
            else:
                i += 1
                continue

            if arg_name in self.types:
                arg_value = self._convert_type(arg_name, arg_value)

            self.arguments[arg_name] = arg_value

        missing_args = self.required - set(self.arguments.keys())
        if missing_args:
            return False, missing_args
        else:
            return True, None

    def get_argument(self, key):
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        self.types[arg] = arg_type
        if required:
            self.required.add(arg)

    def _convert_type(self, arg, value):
        if self.types[arg] == int:
            try:
                return int(value)
            except ValueError:
                pass
        elif self.types[arg] == float:
            try:
                return float(value)
            except ValueError:
                pass
        elif self.types[arg] == bool:
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
        return value