class BitStatusUtil:
    @staticmethod
    def add(states, stat):
        """
        Add a status to the current status, and check the parameters whether they are legal.
        :return: The status after adding the status, int.
        """
        BitStatusUtil.check(states)
        BitStatusUtil.check(stat)
        # Use bitwise OR to add the status
        return states | stat

    @staticmethod
    def has(states, stat):
        """
        Check if the current status contains the specified status, and check the parameters whether they are legal.
        :return: True if the current status contains the specified status, otherwise False, bool.
        """
        BitStatusUtil.check(states)
        BitStatusUtil.check(stat)
        # Use bitwise AND to check if the status contains the specified status
        return (states & stat) == stat

    @staticmethod
    def remove(states, stat):
        """
        Remove the specified status from the current status, and check the parameters whether they are legal.
        :return: The status after removing the specified status, int.
        """
        BitStatusUtil.check(states)
        BitStatusUtil.check(stat)
        # Use bitwise AND with NOT to remove the status
        return states & ~stat

    @staticmethod
    def check(args):
        """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even, if not, raise ValueError.
        :return: None.
        """
        if args < 0 or args % 2 != 0:
            raise ValueError("Argument must be a non-negative even integer.")