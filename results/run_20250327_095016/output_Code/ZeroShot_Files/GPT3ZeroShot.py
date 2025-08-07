import itertools
import math

class ArrangementCalculator:
    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        """
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :return: int, the count of arrangements.
        """
        if m is None or n == m:
            return ArrangementCalculator.factorial(n)
        return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)

    @staticmethod
    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :return: int, the count of all arrangements.
        """
        total = 0
        for m in range(1, n + 1):
            total += ArrangementCalculator.count(n, m)
        return total

    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal datas.
        :return: List, a list of arrangements.
        """
        if m is None:
            m = len(self.datas)
        return list(itertools.permutations(self.datas, m))

    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        """
        all_arrangements = []
        for m in range(1, len(self.datas) + 1):
            all_arrangements.extend(self.select(m))
        return all_arrangements

    @staticmethod
    def factorial(n):
        """
        Calculates the factorial of a given number.
        :return: int, the factorial of the given number.
        """
        return math.factorial(n)