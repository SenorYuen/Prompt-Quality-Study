# This is a utility class that provides methods for manipulating and checking status using bitwise operations.

class BitStatusUtil:
    @staticmethod
    def add(states, stat):
        # Check if the parameters are legal
        BitStatusUtil.check(states)
        BitStatusUtil.check(stat)
        
        # Add a status to the current status using bitwise OR operation
        return states | stat

    @staticmethod
    def has(states, stat):
        # Check if the parameters are legal
        BitStatusUtil.check(states)
        BitStatusUtil.check(stat)
        
        # Check if the current status contains the specified status using bitwise AND operation
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        # Check if the parameters are legal
        BitStatusUtil.check(states)
        BitStatusUtil.check(stat)
        
        # Remove the specified status from the current status using bitwise AND and NOT operations
        return states & (~stat)

    @staticmethod
    def check(args):
        # Check if the parameter is greater than or equal to 0
        if args < 0:
            raise ValueError("Parameter must be greater than or equal to 0")
        
        # Check if the parameter is even
        if args % 2 != 0:
            raise ValueError("Parameter must be even")