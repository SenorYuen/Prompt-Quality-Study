import math
import numpy as np
from scipy import stats


class Statistics3:
    @staticmethod
    def median(data):
        return np.median(data)

    @staticmethod
    def mode(data):
        return stats.mode(data)[0].tolist()

    @staticmethod
    def correlation(x, y):
        return np.corrcoef(x, y)[0, 1]

    @staticmethod
    def mean(data):
        return np.mean(data)

    @staticmethod
    def correlation_matrix(data):
        return np.corrcoef(data).tolist()

    @staticmethod
    def standard_deviation(data):
        return np.std(data)

    @staticmethod
    def z_score(data):
        mean = np.mean(data)
        std_dev = np.std(data)
        return [(x - mean) / std_dev for x in data]