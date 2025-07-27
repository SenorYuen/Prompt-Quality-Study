import math
from typing import List

class CombinationCalculator:
    def __init__(self, datas: List[str]):
        # Initialize the calculator with a list of data
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        # Calculate the number of combinations for a specific count using the formula n! / (m! * (n-m)!)
        if m > n:
            return 0
        result = math.comb(n, m)
        return result

    @staticmethod
    def count_all(n: int) -> int:
        # Calculate the number of all possible combinations, which is 2^n
        result = 2 ** n
        # If the number of combinations is greater than 2^63-1, return float("inf")
        if result > 2 ** 63 - 1:
            return float("inf")
        return result

    def select(self, m: int) -> List[List[str]]:
        # Generate combinations with a specified number of elements
        result = []
        self._select(0, [], 0, result, m)
        return result

    def select_all(self) -> List[List[str]]:
        # Generate all possible combinations of selecting elements from the given data list
        result = []
        for i in range(len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]], m: int):
        # Generate combinations with a specified number of elements by recursion
        if resultIndex == m:
            # If the current combination has the specified number of elements, add it to the result
            result.append(resultList[:])
            return
        for i in range(dataIndex, len(self.datas)):
            # Add the current element to the current combination
            resultList.append(self.datas[i])
            # Recursively generate combinations with the remaining elements
            self._select(i + 1, resultList, resultIndex + 1, result, m)
            # Remove the current element from the current combination for backtracking
            resultList.pop()