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
        count = 0
        for i in range(1, n + 1):
            count += ArrangementCalculator.count(n, i)
        return count

    def select(self, m=None):
        if m is None:
            m = len(self.datas)
        return self._permute(self.datas, m)

    def select_all(self):
        all_selections = []
        for i in range(1, len(self.datas) + 1):
            all_selections.extend(self._permute(self.datas, i))
        return all_selections

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def _permute(self, elements, m):
        if m == 0:
            return [[]]
        permutations = []
        for i in range(len(elements)):
            elem = elements[i]
            rest_elems = elements[:i] + elements[i+1:]
            for p in self._permute(rest_elems, m - 1):
                permutations.append([elem] + p)
        return permutations