import itertools
import math

class ArrangementCalculator:
    def __init__(self, datas):
        # Initialize the ArrangementCalculator object with a list of datas
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        # If m is not provided or n equals m, return factorial(n)
        if m is None or n == m:
            return ArrangementCalculator.factorial(n)
        # Calculate the number of arrangements by choosing m items from n items (permutations)
        else:
            return math.factorial(n) // math.factorial(n - m)

    @staticmethod
    def count_all(n):
        # Calculate the total number of all possible arrangements by choosing at least 1 item and at most n items from n items
        total_count = 0
        for i in range(1, n + 1):
            total_count += ArrangementCalculator.count(n, i)
        return total_count

    def select(self, m=None):
        # If m is not provided, set m to the length of the internal datas
        if m is None:
            m = len(self.datas)
        # Generate a list of arrangements by selecting m items from the internal datas
        return list(itertools.permutations(self.datas, m))

    def select_all(self):
        # Generate a list of all arrangements by selecting at least 1 item and at most the number of internal datas
        all_arrangements = []
        for i in range(1, len(self.datas) + 1):
            all_arrangements.extend(self.select(i))
        return all_arrangements

    @staticmethod
    def factorial(n):
        # Calculate the factorial of a given number
        return math.factorial(n)