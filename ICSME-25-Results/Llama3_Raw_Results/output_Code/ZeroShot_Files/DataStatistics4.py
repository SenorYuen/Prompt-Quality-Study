import math

class DataStatistics4:

    # Calculate the correlation coefficient of two sets of data
    @staticmethod
    def correlation_coefficient(data1, data2):
        # Calculate the means of the two datasets
        mean1 = sum(data1) / len(data1)
        mean2 = sum(data2) / len(data2)

        # Calculate the deviations from the mean for each dataset
        deviations1 = [x - mean1 for x in data1]
        deviations2 = [x - mean2 for x in data2]

        # Calculate the covariance and the variances
        covariance = sum(x * y for x, y in zip(deviations1, deviations2)) / len(data1)
        variance1 = sum(x ** 2 for x in deviations1) / len(data1)
        variance2 = sum(x ** 2 for x in deviations2) / len(data2)

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

        # Calculate the skewness
        skewness = sum(x ** 3 for x in deviations) / len(data) / (variance ** 1.5)
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

        # Calculate the kurtosis
        kurtosis = sum(x ** 4 for x in deviations) / len(data) / (variance ** 2) - 3
        return kurtosis

    # Calculate the probability density function (PDF) of a set of data under a normal distribution
    @staticmethod
    def pdf(data, mu, sigma):
        # Calculate the PDF for each data point
        pdf = [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) for x in data]
        return pdf

# Example usage
if __name__ == "__main__":
    data1 = [1, 2, 3, 4, 5]
    data2 = [2, 3, 5, 7, 11]
    print("Correlation Coefficient:", DataStatistics4.correlation_coefficient(data1, data2))
    print("Skewness:", DataStatistics4.skewness(data1))
    print("Kurtosis:", DataStatistics4.kurtosis(data1))
    print("PDF:", DataStatistics4.pdf(data1, 3, 1))