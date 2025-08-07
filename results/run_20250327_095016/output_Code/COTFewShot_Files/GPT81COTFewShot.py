import math
from collections import Counter

class Statistics3:
    @staticmethod
    def median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]

    @staticmethod
    def mode(data):
        count = Counter(data)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]

    @staticmethod
    def correlation(x, y):
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
        std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))
        return covariance / (std_x * std_y)

    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        n = len(data)
        matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = Statistics3.correlation(data[i], data[j])
        return matrix

    @staticmethod
    def standard_deviation(data):
        mean = Statistics3.mean(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean) / std_dev for x in data]