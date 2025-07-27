import numpy as np

class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        if isinstance(data, tuple):
            actual_result, ground_truth_num = data
            reciprocal_ranks = []
            for i, result in enumerate(actual_result):
                if result == 1:
                    reciprocal_ranks.append(1 / (i + 1))
            if reciprocal_ranks:
                mrr_value = np.mean(reciprocal_ranks)
            else:
                mrr_value = 0
            return mrr_value, [mrr_value]
        elif isinstance(data, list):
            mrr_values = []
            precision_values = []
            for item in data:
                mrr_value, _ = MetricsCalculator2.mrr(item)
                mrr_values.append(mrr_value)
                precision_values.append(mrr_value)
            return np.mean(mrr_values), precision_values
        else:
            raise ValueError("Invalid input data")

    @staticmethod
    def map(data):
        if isinstance(data, tuple):
            actual_result, ground_truth_num = data
            precision_values = []
            correct_count = 0
            for i, result in enumerate(actual_result):
                if result == 1:
                    correct_count += 1
                    precision_values.append(correct_count / (i + 1))
            if precision_values:
                map_value = np.mean(precision_values)
            else:
                map_value = 0
            return map_value, [map_value]
        elif isinstance(data, list):
            map_values = []
            precision_values = []
            for item in data:
                map_value, _ = MetricsCalculator2.map(item)
                map_values.append(map_value)
                precision_values.append(map_value)
            return np.mean(map_values), precision_values
        else:
            raise ValueError("Invalid input data")