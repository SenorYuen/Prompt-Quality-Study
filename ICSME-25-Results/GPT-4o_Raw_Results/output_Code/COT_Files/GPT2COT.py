class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        args = command_string.split()
        missing_args = set(self.required)
        for i in range(len(args)):
            if args[i].startswith('--'):
                key, value = args[i][2:].split('=')
                self.arguments[key] = self._convert_type(key, value)
                missing_args.discard(key)
            elif args[i].startswith('-'):
                key = args[i][1:]
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    self.arguments[key] = self._convert_type(key, args[i + 1])
                    missing_args.discard(key)
                else:
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