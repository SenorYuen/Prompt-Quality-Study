import numpy as np

class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        # Check if input data is a tuple or a list of tuples
        if isinstance(data, tuple):
            # Calculate MRR for a single tuple
            actual_result, ground_truth_num = data
            reciprocal_ranks = []
            for i, result in enumerate(actual_result):
                if result == 1:
                    reciprocal_ranks.append(1 / (i + 1))
            mrr_value = np.mean(reciprocal_ranks) if reciprocal_ranks else 0
            precision_values = [mrr_value]
            return mrr_value, precision_values
        elif isinstance(data, list):
            # Calculate MRR for a list of tuples
            mrr_values = []
            precision_values = []
            for item in data:
                mrr_value, precision_value = MetricsCalculator2.mrr(item)
                mrr_values.append(mrr_value)
                precision_values.append(precision_value[0])
            average_mrr = np.mean(mrr_values)
            return average_mrr, precision_values
        else:
            raise ValueError("Invalid input data")

    @staticmethod
    def map(data):
        # Check if input data is a tuple or a list of tuples
        if isinstance(data, tuple):
            # Calculate MAP for a single tuple
            actual_result, ground_truth_num = data
            precision_values = []
            true_positives = 0
            for i, result in enumerate(actual_result):
                true_positives += result
                precision = true_positives / (i + 1)
                precision_values.append(precision)
            average_precision = np.mean(precision_values) if precision_values else 0
            return average_precision, [average_precision]
        elif isinstance(data, list):
            # Calculate MAP for a list of tuples
            map_values = []
            precision_values = []
            for item in data:
                average_precision, precision_value = MetricsCalculator2.map(item)
                map_values.append(average_precision)
                precision_values.append(precision_value[0])
            average_map = np.mean(map_values)
            return average_map, precision_values
        else:
            raise ValueError("Invalid input data")