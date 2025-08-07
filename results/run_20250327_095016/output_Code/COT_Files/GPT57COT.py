import numpy as np

class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        if isinstance(data[0], list):
            mrr_values = []
            for item in data:
                actual, ground_truth_num = item
                reciprocal_rank = 0
                for idx, val in enumerate(actual):
                    if val == 1:
                        reciprocal_rank = 1 / (idx + 1)
                        break
                mrr_values.append(reciprocal_rank)
            return np.mean(mrr_values), mrr_values
        else:
            actual, ground_truth_num = data
            for idx, val in enumerate(actual):
                if val == 1:
                    return 1 / (idx + 1), [1 / (idx + 1)]
            return 0, [0]

    @staticmethod
    def map(data):
        if isinstance(data[0], list):
            map_values = []
            for item in data:
                actual, ground_truth_num = item
                num_hits = 0
                sum_precisions = 0
                for idx, val in enumerate(actual):
                    if val == 1:
                        num_hits += 1
                        sum_precisions += num_hits / (idx + 1)
                average_precision = sum_precisions / ground_truth_num
                map_values.append(average_precision)
            return np.mean(map_values), map_values
        else:
            actual, ground_truth_num = data
            num_hits = 0
            sum_precisions = 0
            for idx, val in enumerate(actual):
                if val == 1:
                    num_hits += 1
                    sum_precisions += num_hits / (idx + 1)
            average_precision = sum_precisions / ground_truth_num
            return average_precision, [average_precision]