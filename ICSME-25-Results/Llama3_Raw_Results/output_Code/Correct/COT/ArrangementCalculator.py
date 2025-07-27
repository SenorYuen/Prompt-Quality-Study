class ArrangementCalculator:
    def __init__(self, datas):
        # Initialize the ArrangementCalculator object with a list of datas
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        # Count the number of arrangements by choosing m items from n items (permutations)
        if m is None:
            m = n
        # Calculate the permutation using the formula n! / (n-m)!
        return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)

    @staticmethod
    def count_all(n):
        # Count the total number of all possible arrangements by choosing at least 1 item and at most n items from n items
        total = 0
        for m in range(1, n + 1):
            total += ArrangementCalculator.count(n, m)
        return total

    def select(self, m=None):
        # Generate a list of arrangements by selecting m items from the internal datas
        if m is None:
            m = len(self.datas)
        # Use recursion to generate all permutations
        def permute(datas, m):
            if m == 1:
                return [[data] for data in datas]
            result = []
            for i, data in enumerate(datas):
                rest = datas[:i] + datas[i + 1:]
                for p in permute(rest, m - 1):
                    result.append([data] + p)
            return result
        return permute(self.datas, m)

    def select_all(self):
        # Generate a list of all arrangements by selecting at least 1 item and at most the number of internal datas
        total = []
        for m in range(1, len(self.datas) + 1):
            total.extend(self.select(m))
        return total

    @staticmethod
    def factorial(n):
        # Calculate the factorial of a given number
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result