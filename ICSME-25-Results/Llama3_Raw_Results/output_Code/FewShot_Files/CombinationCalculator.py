import math
from typing import List
import itertools

class CombinationCalculator:
    """
    This is a class that provides methods to calculate the number of combinations for a specific count, 
    calculate all possible combinations, and generate combinations with a specified number of elements.
    """

    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        """
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        # Calculate the number of combinations using the formula n! / (m! * (n-m)!)
        if n < m:
            return 0
        return math.comb(n, m)

    @staticmethod
    def count_all(n: int) -> int:
        # Calculate the number of all possible combinations using the formula 2^n - 1
        # If the number of combinations is greater than 2^63-1, return float("inf")
        count = 2 ** n - 1
        if count > 2 ** 63 - 1:
            return float("inf")
        return count

    def select(self, m: int) -> List[List[str]]:
        # Generate combinations with a specified number of elements using itertools.combinations
        return [list(combination) for combination in itertools.combinations(self.datas, m)]

    def select_all(self) -> List[List[str]]:
        # Generate all possible combinations of selecting elements from the given data list
        # Use the select method to generate combinations of each size
        all_combinations = []
        for i in range(1, len(self.datas) + 1):
            all_combinations.extend(self.select(i))
        return all_combinations

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]], m: int):
        # Generate combinations with a specified number of elements by recursion
        if resultIndex == m:
            result.append(resultList[:])
            return
        for i in range(dataIndex, len(self.datas)):
            resultList[resultIndex] = self.datas[i]
            self._select(i + 1, resultList, resultIndex + 1, result, m)

# Example usage
calc = CombinationCalculator(["A", "B", "C", "D"])
print(CombinationCalculator.count(4, 2))  # Output: 6
print(CombinationCalculator.count_all(4))  # Output: 15
print(calc.select(2))  # Output: [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]
print(calc.select_all())  # Output: [['A'], ['B'], ['C'], ['D'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D'], ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'C', 'D'], ['B', 'C', 'D'], ['A', 'B', 'C', 'D']]
result = []
calc._select(0, [None] * 2, 0, result, 2)
print(result)  # Output: [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'D']]