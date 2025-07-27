import math
import statistics
from scipy.stats import pearsonr
import numpy as np

class Statistics3:
    @staticmethod
    def median(data):
        return statistics.median(data)

    @staticmethod
    def mode(data):
        return statistics.multimode(data)

    @staticmethod
    def correlation(x, y):
        return pearsonr(x, y)[0]

    @staticmethod
    def mean(data):
        return statistics.mean(data)

    @staticmethod
    def correlation_matrix(data):
        return np.corrcoef(data).tolist()

    @staticmethod
    def standard_deviation(data):
        return statistics.stdev(data)

    @staticmethod
    def z_score(data):
        mean = statistics.mean(data)
        std_dev = statistics.stdev(data)
        return [(x - mean) / std_dev for x in data]