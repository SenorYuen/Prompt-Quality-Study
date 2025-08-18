'''
# This is a utility class that provides methods for manipulating and checking status using bitwise operations.

class BitStatusUtil:
    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status,and check the parameters wheather they are legal.
        :return: The status after adding the status,int.
        """

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status,and check the parameters wheather they are legal.
        :return: True if the current status contains the specified status,otherwise False,bool.
        """

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status,and check the parameters wheather they are legal.
        :return: The status after removing the specified status,int.
        """

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even,if not,raise ValueError.
        :return: None.
        """
'''


class BitStatusUtil:
    @staticmethod
    def add(states, stat):
        BitStatusUtil.check([states, stat])
        return states | stat

    @staticmethod
    def has(states, stat):
        BitStatusUtil.check([states, stat])
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        BitStatusUtil.check([states, stat])
        if BitStatusUtil.has(states, stat):
            return states ^ stat
        return states

    @staticmethod
    def check(args):
        for arg in args:
            if arg < 0:
                raise ValueError(f"{arg} must be greater than or equal to 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")

