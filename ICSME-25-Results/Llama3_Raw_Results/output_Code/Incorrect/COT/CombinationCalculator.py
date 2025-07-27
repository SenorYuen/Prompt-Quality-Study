import math
from typing import List

class CombinationCalculator:
    def __init__(self, datas: List[str]):
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        return math.comb(n, m)

    @staticmethod
    def count_all(n: int) -> int:
        total_combinations = sum(math.comb(n, i) for i in range(n + 1))
        return total_combinations if total_combinations <= 2**63 - 1 else float("inf")

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        if resultIndex == len(resultList):
            result.append(resultList[:])
            return
        for i in range(dataIndex, len(self.datas)):
            resultList[resultIndex] = self.datas[i]
            self._select(i + 1, resultList, resultIndex + 1, result)

    def select(self, m: int) -> List[List[str]]:
        result = []
        self._select(0, [None] * m, 0, result)
        return result

    def select_all(self) -> List[List[str]]:
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result