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
        data_counter = Counter(data)
        max_count = max(data_counter.values())
        return [k for k, v in data_counter.items() if v == max_count]

    @staticmethod
    def correlation(x, y):
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        stddev_x = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
        stddev_y = math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
        return covariance / (stddev_x * stddev_y)

    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        size = len(data)
        corr_matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1.0)
                else:
                    row.append(Statistics3.correlation(data[i], data[j]))
            corr_matrix.append(row)
        return corr_matrix

    @staticmethod
    def standard_deviation(data):
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        mean_value = Statistics3.mean(data)
        stddev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / stddev for x in data]