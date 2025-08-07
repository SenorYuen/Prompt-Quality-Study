import math
from collections import Counter

class Statistics3:
    @staticmethod
    def median(data):
        """
        calculates the median of the given list.
        :return: the median of the given list, float.
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            # If even, return the average of the middle two numbers
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            # If odd, return the middle number
            return sorted_data[mid]

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :return: the mode of the given list, list.
        """
        count = Counter(data)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]

    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :return: the correlation of the given list, float.
        """
        n = len(x)
        if n != len(y):
            raise ValueError("Lists must have the same length")
        
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)) * sum((y[i] - mean_y) ** 2 for i in range(n)))
        
        if denominator == 0:
            return 0
        
        return numerator / denominator

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :return: the mean of the given list, float.
        """
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :return: the correlation matrix of the given list, list.
        """
        size = len(data)
        matrix = [[0] * size for _ in range(size)]
        
        for i in range(size):
            for j in range(size):
                if i == j:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = Statistics3.correlation(data[i], data[j])
        
        return matrix

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :return: the standard deviation of the given list, float.
        """
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :return: the z-score of the given list, list.
        """
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        
        if std_dev == 0:
            return [0] * len(data)
        
        return [(x - mean_value) / std_dev for x in data]