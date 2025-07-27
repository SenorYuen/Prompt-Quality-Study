import numpy as np

class DataStatistics2:
    def __init__(self, data):
        self.data = np.array(data)

    def get_sum(self):
        return float(np.sum(self.data))

    def get_min(self):
        return float(np.min(self.data))

    def get_max(self):
        return float(np.max(self.data))

    def get_variance(self):
        return round(float(np.var(self.data)), 2)

    def get_std_deviation(self):
        return round(float(np.std(self.data)), 2)

    def get_correlation(self):
        return float(np.corrcoef(self.data, self.data)[0, 1])