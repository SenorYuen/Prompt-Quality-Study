import math
import numpy as np
from scipy.stats import norm

class DataStatistics4:
    @staticmethod
    def correlation_coefficient(data1, data2):
        mean1 = np.mean(data1)
        mean2 = np.mean(data2)
        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
        denominator = math.sqrt(sum((x - mean1) ** 2 for x in data1)) * math.sqrt(sum((y - mean2) ** 2 for y in data2))
        return numerator / denominator

    @staticmethod
    def skewness(data):
        mean = np.mean(data)
        variance = np.var(data)
        std_dev = math.sqrt(variance)
        numerator = sum((x - mean) ** 3 for x in data)
        denominator = len(data) * (std_dev ** 3)
        return numerator / denominator

    @staticmethod
    def kurtosis(data):
        mean = np.mean(data)
        variance = np.var(data)
        std_dev = math.sqrt(variance)
        numerator = sum((x - mean) ** 4 for x in data)
        denominator = len(data) * (std_dev ** 4)
        return numerator / denominator - 3

    @staticmethod
    def pdf(data, mu, sigma):
        return [norm.pdf(x, mu, sigma) for x in data]