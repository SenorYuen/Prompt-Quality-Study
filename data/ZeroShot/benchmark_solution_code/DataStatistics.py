'''
# This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.

from collections import Counter

class DataStatistics:
    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :return:float, the mean value
        """

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :return:float, the median value
        """

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :return:float, the mode
        """
'''

from collections import Counter


class DataStatistics:
    def mean(self, data):
        return round(sum(data) / len(data), 2)

    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            middle = n // 2
            return round((sorted_data[middle - 1] + sorted_data[middle]) / 2, 2)
        else:
            middle = n // 2
            return sorted_data[middle]

    def mode(self, data):
        counter = Counter(data)
        mode_count = max(counter.values())
        mode = [x for x, count in counter.items() if count == mode_count]
        return mode
