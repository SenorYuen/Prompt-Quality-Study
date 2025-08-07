import math

class DataStatistics4:

    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :return: The correlation coefficient, float.
        """
        n = len(data1)
        mean1 = sum(data1) / n
        mean2 = sum(data2) / n
        
        # Calculate covariance
        covariance = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
        
        # Calculate standard deviations
        stddev1 = math.sqrt(sum((x - mean1) ** 2 for x in data1))
        stddev2 = math.sqrt(sum((x - mean2) ** 2 for x in data2))
        
        # Calculate correlation coefficient
        correlation = covariance / (stddev1 * stddev2)
        return correlation

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :return: The skewness, float.
        """
        n = len(data)
        mean = sum(data) / n
        m3 = sum((x - mean) ** 3 for x in data) / n
        m2 = sum((x - mean) ** 2 for x in data) / n
        skewness = m3 / (m2 ** 1.5)
        return skewness

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :return: The kurtosis, float.
        """
        n = len(data)
        mean = sum(data) / n
        m4 = sum((x - mean) ** 4 for x in data) / n
        m2 = sum((x - mean) ** 2 for x in data) / n
        kurtosis = m4 / (m2 ** 2) - 3  # Excess kurtosis
        return kurtosis

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :return: The probability density function (PDF), list.
        """
        pdf_values = []
        for x in data:
            # Calculate the PDF for each data point
            exponent = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
            pdf_value = (1 / (math.sqrt(2 * math.pi) * sigma)) * exponent
            pdf_values.append(pdf_value)
        return pdf_values