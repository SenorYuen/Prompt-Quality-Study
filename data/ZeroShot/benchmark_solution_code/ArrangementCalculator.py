'''
# The Arrangement class provides permutation calculations and selection operations for a given set of data elements.

import itertools

class ArrangementCalculator:
    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        """

    @staticmethod
    def count(n, m=None):
        """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :return: int, the count of arrangements.
        """

    @staticmethod
    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :return: int, the count of all arrangements.
        """


    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal datas.
        :return: List, a list of arrangements.
        """


    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        """


    @staticmethod
    def factorial(n):
        """
        Calculates the factorial of a given number.
        :return: int, the factorial of the given number.
        """

'''

import itertools


class ArrangementCalculator:
    def __init__(self, datas):
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        if m is None or n == m:
            return ArrangementCalculator.factorial(n)
        else:
            return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)

    @staticmethod
    def count_all(n):
        total = 0
        for i in range(1, n + 1):
            total += ArrangementCalculator.count(n, i)
        return total

    def select(self, m=None):
        if m is None:
            m = len(self.datas)
        result = []
        for permutation in itertools.permutations(self.datas, m):
            result.append(list(permutation))
        return result

    def select_all(self):
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


