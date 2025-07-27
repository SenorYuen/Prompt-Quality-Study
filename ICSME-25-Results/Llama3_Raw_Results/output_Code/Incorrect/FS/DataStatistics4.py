import math

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, 
    including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """

    # Calculate the correlation coefficient of two sets of data
    @staticmethod
    def correlation_coefficient(data1, data2):
        # Check if the lengths of the two datasets are equal
        if len(data1) != len(data2):
            raise ValueError("Both datasets must have the same length")

        # Calculate the means of the two datasets
        mean1 = sum(data1) / len(data1)
        mean2 = sum(data2) / len(data2)

        # Calculate the deviations from the means
        deviations1 = [x - mean1 for x in data1]
        deviations2 = [x - mean2 for x in data2]

        # Calculate the covariance and the variances
        covariance = sum(x * y for x, y in zip(deviations1, deviations2))
        variance1 = sum(x ** 2 for x in deviations1)
        variance2 = sum(x ** 2 for x in deviations2)

        # Calculate the correlation coefficient
        correlation_coefficient = covariance / math.sqrt(variance1 * variance2)

        return correlation_coefficient

    # Calculate the skewness of a set of data
    @staticmethod
    def skewness(data):
        # Calculate the mean of the dataset
        mean = sum(data) / len(data)

        # Calculate the deviations from the mean
        deviations = [x - mean for x in data]

        # Calculate the variance
        variance = sum(x ** 2 for x in deviations) / len(data)

        # Calculate the standard deviation
        std_dev = math.sqrt(variance)

        # Calculate the skewness
        skewness = sum((x - mean) ** 3 for x in data) / (len(data) * std_dev ** 3)

        return skewness

    # Calculate the kurtosis of a set of data
    @staticmethod
    def kurtosis(data):
        # Calculate the mean of the dataset
        mean = sum(data) / len(data)

        # Calculate the deviations from the mean
        deviations = [x - mean for x in data]

        # Calculate the variance
        variance = sum(x ** 2 for x in deviations) / len(data)

        # Calculate the standard deviation
        std_dev = math.sqrt(variance)

        # Calculate the kurtosis
        kurtosis = sum((x - mean) ** 4 for x in data) / (len(data) * std_dev ** 4) - 3

        return kurtosis

    # Calculate the probability density function (PDF) of a set of data under a normal distribution
    @staticmethod
    def pdf(data, mu, sigma):
        # Calculate the PDF for each data point
        pdf_values = [math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi)) for x in data]

        return pdf_values