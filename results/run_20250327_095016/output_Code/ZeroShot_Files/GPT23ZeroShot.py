import math
from typing import List
from itertools import combinations

class CombinationCalculator:
    def __init__(self, datas: List[str]):
        """
        Initialize the calculator with a list of data.
        """
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        """
        Calculate the number of combinations for a specific count.
        :return: The number of combinations, int.
        """
        if m > n:
            return 0
        return math.comb(n, m)

    @staticmethod
    def count_all(n: int) -> int:
        """
        Calculate the number of all possible combinations.
        :return: The number of all possible combinations, int, if the number of combinations is greater than 2^63-1, return float("inf").
        """
        total_combinations = sum(math.comb(n, i) for i in range(n + 1))
        return total_combinations if total_combinations <= 2**63 - 1 else float("inf")

    def select(self, m: int) -> List[List[str]]:
        """
        Generate combinations with a specified number of elements.
        :return: A list of combinations, List[List[str]].
        """
        if m > len(self.datas):
            return []
        return [list(comb) for comb in combinations(self.datas, m)]

    def select_all(self) -> List[List[str]]:
        """
        Generate all possible combinations of selecting elements from the given data list, and it uses the select method.
        :return: A list of combinations, List[List[str]].
        """
        result = []
        for i in range(len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        """
        Generate combinations with a specified number of elements by recursion.
        :return: None.
        """
        if resultIndex == len(resultList):
            result.append(resultList.copy())
            return
        if dataIndex >= len(self.datas):
            return

        # Include the current element
        resultList[resultIndex] = self.datas[dataIndex]
        self._select(dataIndex + 1, resultList, resultIndex + 1, result)

        # Exclude the current element
        self._select(dataIndex + 1, resultList, resultIndex, result)