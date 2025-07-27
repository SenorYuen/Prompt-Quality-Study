import math
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        # Sort the data in ascending order
        sorted_data = sorted(data)
        n = len(sorted_data)
        
        # If the length of the data is even, the median is the average of the two middle numbers
        if n % 2 == 0:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        # If the length of the data is odd, the median is the middle number
        else:
            median = sorted_data[n // 2]
        return median

    @staticmethod
    def mode(data):
        # Count the frequency of each number in the data
        frequency = Counter(data)
        
        # Find the number with the highest frequency
        max_frequency = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_frequency]
        return modes

    @staticmethod
    def correlation(x, y):
        # Calculate the means of x and y
        mean_x = sum(x) / len(x)
        mean_y = sum(y) / len(y)
        
        # Calculate the deviations from the means
        deviations_x = [xi - mean_x for xi in x]
        deviations_y = [yi - mean_y for yi in y]
        
        # Calculate the covariance and the variances
        covariance = sum(xi * yi for xi, yi in zip(deviations_x, deviations_y)) / len(x)
        variance_x = sum(xi ** 2 for xi in deviations_x) / len(x)
        variance_y = sum(yi ** 2 for yi in deviations_y) / len(y)
        
        # Calculate the correlation coefficient
        correlation_coefficient = covariance / math.sqrt(variance_x * variance_y)
        return correlation_coefficient

    @staticmethod
    def mean(data):
        # Calculate the sum of the data
        total = sum(data)
        
        # Calculate the mean
        mean = total / len(data)
        return mean

    @staticmethod
    def correlation_matrix(data):
        # Calculate the correlation matrix
        correlation_matrix = [[Statistics3.correlation(x, y) for y in zip(*data)] for x in zip(*data)]
        return correlation_matrix

    @staticmethod
    def standard_deviation(data):
        # Calculate the mean
        mean = Statistics3.mean(data)
        
        # Calculate the variance
        variance = sum((xi - mean) ** 2 for xi in data) / len(data)
        
        # Calculate the standard deviation
        standard_deviation = math.sqrt(variance)
        return standard_deviation

    @staticmethod
    def z_score(data):
        # Calculate the mean and standard deviation
        mean = Statistics3.mean(data)
        standard_deviation = Statistics3.standard_deviation(data)
        
        # Calculate the z-scores
        z_scores = [(xi - mean) / standard_deviation for xi in data]
        return z_scores