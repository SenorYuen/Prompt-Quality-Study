class BitStatusUtil:
    @staticmethod
    def add(states, stat):
        # Check if parameters are legal
        BitStatusUtil.check([states, stat])
        
        # Add the status to the current status using bitwise OR operation
        return states | stat

    @staticmethod
    def has(states, stat):
        # Check if parameters are legal
        BitStatusUtil.check([states, stat])
        
        # Check if the current status contains the specified status using bitwise AND operation
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        # Check if parameters are legal
        BitStatusUtil.check([states, stat])
        
        # Remove the specified status from the current status using bitwise AND and NOT operations
        return states & ~stat

    @staticmethod
    def check(args):
        # Check if all parameters are greater than or equal to 0 and even
        for arg in args:
            if arg < 0:
                raise ValueError(f"{arg} not greater than or equal to 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")