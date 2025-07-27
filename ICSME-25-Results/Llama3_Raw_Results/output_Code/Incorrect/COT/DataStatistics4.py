import math

class DataStatistics4:
    @staticmethod
    def correlation_coefficient(data1, data2):
        n = len(data1)
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
        denominator = math.sqrt(sum((x - mean1) ** 2 for x in data1)) * math.sqrt(sum((y - mean2) ** 2 for y in data2))
        return numerator / denominator

    @staticmethod
    def skewness(data):
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)
        numerator = sum((x - mean) ** 3 for x in data)
        return numerator / (n * std_dev ** 3)

    @staticmethod
    def kurtosis(data):
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)
        numerator = sum((x - mean) ** 4 for x in data)
        return numerator / (n * std_dev ** 4) - 3

    @staticmethod
    def pdf(data, mu, sigma):
        return [math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi)) for x in data]