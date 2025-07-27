# This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.

from collections import Counter
import statistics

class DataStatistics:
    # Calculate the average value of a group of data, accurate to two digits after the Decimal separator
    def mean(self, data):
        # Check if data is empty
        if not data:
            return None
        # Calculate the mean using the statistics library and round to two decimal places
        return round(statistics.mean(data), 2)

    # Calculate the median of a group of data, accurate to two digits after the Decimal separator
    def median(self, data):
        # Check if data is empty
        if not data:
            return None
        # Calculate the median using the statistics library and round to two decimal places
        return round(statistics.median(data), 2)

    # Calculate the mode of a set of data
    def mode(self, data):
        # Check if data is empty
        if not data:
            return None
        # Use Counter to count the frequency of each data point
        counter = Counter(data)
        # Find the data point with the highest frequency
        mode = [k for k, v in counter.items() if v == max(counter.values())]
        # If there are multiple modes, return the smallest one
        return min(mode)

# Example usage:
data_stats = DataStatistics()
data = [1, 2, 3, 4, 4, 5, 5, 5]
print(data_stats.mean(data))  # Output: 3.75
print(data_stats.median(data))  # Output: 4.0
print(data_stats.mode(data))  # Output: 5