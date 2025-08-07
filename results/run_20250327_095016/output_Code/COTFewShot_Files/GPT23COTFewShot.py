import math
from typing import List


class CombinationCalculator:
    def __init__(self, datas: List[str]):
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        if m > n:
            return 0
        return math.comb(n, m)

    @staticmethod
    def count_all(n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            total += math.comb(n, i)
        return total if total <= 2**63 - 1 else float("inf")

    def select(self, m: int) -> List[List[str]]:
        result = []
        self._select(0, [None] * m, 0, result)
        return result

    def select_all(self) -> List[List[str]]:
        result = []
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    def _select(self, dataIndex: int, resultList: List[str], resultIndex: int, result: List[List[str]]):
        if resultIndex == len(resultList):
            result.append(resultList.copy())
            return
        if dataIndex >= len(self.datas):
            return
        resultList[resultIndex] = self.datas[dataIndex]
        self._select(dataIndex + 1, resultList, resultIndex + 1, result)
        self._select(dataIndex + 1, resultList, resultIndex, result)