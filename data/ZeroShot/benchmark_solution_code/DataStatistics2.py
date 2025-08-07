'''
# This is a class for performing data statistics, supporting to get the sum, minimum, maximum, variance, standard deviation, and correlation of a given dataset.

import numpy as np

class DataStatistics2:
    def __init__(self, data):
        """
        Initialize Data List
        """

    def get_sum(self):
        """
        Calculate the sum of data
        :return:float
        """

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        """

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        """

    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        """

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        """

    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        """
'''

import numpy as np


class DataStatistics2:
    def __init__(self, data):
        self.data = np.array(data)

    def get_sum(self):
        return np.sum(self.data)

    def get_min(self):
        return np.min(self.data)

    def get_max(self):
        return np.max(self.data)

    def get_variance(self):
        return round(np.var(self.data), 2)

    def get_std_deviation(self):
        return round(np.std(self.data), 2)

    def get_correlation(self):
        return np.corrcoef(self.data, rowvar=False)



