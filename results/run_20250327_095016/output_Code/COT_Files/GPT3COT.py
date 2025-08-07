class ArrangementCalculator:
    def __init__(self, datas):
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        if m is None:
            m = n
        return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)

    @staticmethod
    def count_all(n):
        total = 0
        for m in range(1, n + 1):
            total += ArrangementCalculator.count(n, m)
        return total

    def select(self, m=None):
        if m is None:
            m = len(self.datas)
        return self._permute(self.datas, m)

    def select_all(self):
        result = []
        for m in range(1, len(self.datas) + 1):
            result.extend(self._permute(self.datas, m))
        return result

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def _permute(self, items, m):
        if m == 0:
            return [[]]
        permutations = []
        for i in range(len(items)):
            for perm in self._permute(items[:i] + items[i+1:], m - 1):
                permutations.append([items[i]] + perm)
        return permutations