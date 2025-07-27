import numpy as np

class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num), ground truth num is the total ground num.
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the average recall on all list. The second return value is a list of precision for each input.
        """
        def calculate_mrr(single_data):
            actual, _ = single_data
            for i, value in enumerate(actual):
                if value == 1:
                    return 1 / (i + 1)
            return 0

        if isinstance(data[0], tuple):
            mrr_values = [calculate_mrr(d) for d in data]
            return np.mean(mrr_values), mrr_values
        else:
            return calculate_mrr(data), [calculate_mrr(data)]

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num), ground truth num is the total ground num.
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the average recall on all list. The second return value is a list of precision for each input.
        """
        def calculate_ap(single_data):
            actual, total_ground_truth = single_data
            correct_count = 0
            precision_sum = 0
            for i, value in enumerate(actual):
                if value == 1:
                    correct_count += 1
                    precision_sum += correct_count / (i + 1)
            return precision_sum / total_ground_truth if total_ground_truth > 0 else 0

        if isinstance(data[0], tuple):
            ap_values = [calculate_ap(d) for d in data]
            return np.mean(ap_values), ap_values
        else:
            return calculate_ap(data), [calculate_ap(data)]