import numpy as np

class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        if isinstance(data[0], list):
            mrr_list = []
            for d in data:
                actual, _ = d
                for rank, value in enumerate(actual, start=1):
                    if value == 1:
                        mrr_list.append(1 / rank)
                        break
            return np.mean(mrr_list), mrr_list
        else:
            actual, _ = data
            for rank, value in enumerate(actual, start=1):
                if value == 1:
                    return 1 / rank, [1 / rank]
            return 0.0, [0.0]

    @staticmethod
    def map(data):
        if isinstance(data[0], list):
            ap_list = []
            for d in data:
                actual, ground_truth_num = d
                correct = 0
                precision_sum = 0.0
                for rank, value in enumerate(actual, start=1):
                    if value == 1:
                        correct += 1
                        precision_sum += correct / rank
                ap_list.append(precision_sum / ground_truth_num)
            return np.mean(ap_list), ap_list
        else:
            actual, ground_truth_num = data
            correct = 0
            precision_sum = 0.0
            for rank, value in enumerate(actual, start=1):
                if value == 1:
                    correct += 1
                    precision_sum += correct / rank
            return precision_sum / ground_truth_num, [precision_sum / ground_truth_num]