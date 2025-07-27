# This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.

import math
import statistics
import numpy as np
from scipy import stats

class Statistics3:
    # calculates the median of the given list.
    @staticmethod
    def median(data):
        # Check if the list is empty
        if not data:
            return None
        # Use the statistics module to calculate the median
        return statistics.median(data)

    # calculates the mode of the given list.
    @staticmethod
    def mode(data):
        # Check if the list is empty
        if not data:
            return None
        # Use the statistics module to calculate the mode
        return statistics.multimode(data)

    # calculates the correlation of the given list.
    @staticmethod
    def correlation(x, y):
        # Check if the lists are empty
        if not x or not y:
            return None
        # Check if the lists have the same length
        if len(x) != len(y):
            return None
        # Use the numpy module to calculate the correlation
        return np.corrcoef(x, y)[0, 1]

    # calculates the mean of the given list.
    @staticmethod
    def mean(data):
        # Check if the list is empty
        if not data:
            return None
        # Use the statistics module to calculate the mean
        return statistics.mean(data)

    # calculates the correlation matrix of the given list.
    @staticmethod
    def correlation_matrix(data):
        # Check if the list is empty
        if not data:
            return None
        # Use the numpy module to calculate the correlation matrix
        return np.corrcoef(data)

    # calculates the standard deviation of the given list.
    @staticmethod
    def standard_deviation(data):
        # Check if the list is empty
        if not data:
            return None
        # Use the statistics module to calculate the standard deviation
        return statistics.stdev(data)

    # calculates the z-score of the given list.
    @staticmethod
    def z_score(data):
        # Check if the list is empty
        if not data:
            return None
        # Calculate the mean and standard deviation
        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        # Use a list comprehension to calculate the z-score for each value
        return [(x - mean) / std_dev for x in data]