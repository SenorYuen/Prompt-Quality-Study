import math

class DataStatistics4:
    @staticmethod
    def correlation_coefficient(data1, data2):
        n = len(data1)
        sum1 = sum(data1)
        sum2 = sum(data2)
        sum1_sq = sum([pow(val, 2) for val in data1])
        sum2_sq = sum([pow(val, 2) for val in data2])
        p_sum = sum([data1[i] * data2[i] for i in range(n)])
        num = p_sum - (sum1 * sum2 / n)
        den = math.sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))
        if den == 0:
            return 0
        return num / den

    @staticmethod
    def skewness(data):
        n = len(data)
        mean = sum(data) / n
        m3 = sum([(x - mean) ** 3 for x in data]) / n
        m2 = sum([(x - mean) ** 2 for x in data]) / n
        if m2 == 0:
            return 0
        return m3 / (m2 ** 1.5)

    @staticmethod
    def kurtosis(data):
        n = len(data)
        mean = sum(data) / n
        m4 = sum([(x - mean) ** 4 for x in data]) / n
        m2 = sum([(x - mean) ** 2 for x in data]) / n
        if m2 == 0:
            return 0
        return m4 / (m2 ** 2) - 3

    @staticmethod
    def pdf(data, mu, sigma):
        return [(1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in data]