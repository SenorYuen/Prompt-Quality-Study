import itertools
import math

class ArrangementCalculator:
    """
    The Arrangement class provides permutation calculations and selection operations for a given set of data elements.
    """

    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :param n: int, the total number of items.
        :param m: int, the number of items to be chosen (default=None).
        :return: int, the count of arrangements.
        """
        # If m is not provided, set m to n
        if m is None:
            m = n
        # Calculate the permutation using the formula n! / (n-m)!
        return math.factorial(n) // math.factorial(n - m)

    @staticmethod
    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :param n: int, the total number of items.
        :return: int, the count of all arrangements.
        """
        # Initialize the total count to 0
        total_count = 0
        # Iterate over all possible values of m from 1 to n
        for m in range(1, n + 1):
            # Add the count of arrangements for the current m to the total count
            total_count += ArrangementCalculator.count(n, m)
        return total_count

    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal datas.
        If m is not provided, selects all items.
        :param m: int, the number of items to be chosen (default=None).
        :return: List, a list of arrangements.
        """
        # If m is not provided, set m to the length of the datas
        if m is None:
            m = len(self.datas)
        # Use itertools.permutations to generate all permutations of m items from the datas
        return [list(p) for p in itertools.permutations(self.datas, m)]

    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        """
        # Initialize an empty list to store all arrangements
        all_arrangements = []
        # Iterate over all possible values of m from 1 to the length of the datas
        for m in range(1, len(self.datas) + 1):
            # Add the arrangements for the current m to the list of all arrangements
            all_arrangements.extend(self.select(m))
        return all_arrangements

    @staticmethod
    def factorial(n):
        """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        """
        # Use math.factorial to calculate the factorial
        return math.factorial(n)