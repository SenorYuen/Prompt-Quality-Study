import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, 
    where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        # Check if input data is a tuple or a list of tuples
        if isinstance(data, tuple):
            # Calculate MRR for a single tuple
            actual_result, ground_truth_num = data
            # Find the index of the first correct answer
            correct_answer_index = np.where(np.array(actual_result) == 1)[0]
            if len(correct_answer_index) > 0:
                # Calculate MRR
                mrr_value = 1 / (correct_answer_index[0] + 1)
            else:
                # If no correct answer is found, set MRR to 0
                mrr_value = 0
            return mrr_value, [mrr_value]
        elif isinstance(data, list):
            # Calculate MRR for a list of tuples
            mrr_values = []
            for item in data:
                mrr_value, _ = MetricsCalculator2.mrr(item)
                mrr_values.append(mrr_value)
            # Calculate average MRR
            average_mrr = np.mean(mrr_values)
            return average_mrr, mrr_values
        else:
            # Raise an error if input data is not a tuple or a list of tuples
            raise ValueError("Invalid input data")

    @staticmethod
    def map(data):
        # Check if input data is a tuple or a list of tuples
        if isinstance(data, tuple):
            # Calculate MAP for a single tuple
            actual_result, ground_truth_num = data
            # Calculate precision at each position
            precision_values = []
            correct_answers = 0
            for i, result in enumerate(actual_result):
                if result == 1:
                    correct_answers += 1
                    precision_values.append(correct_answers / (i + 1))
            # Calculate average precision
            if len(precision_values) > 0:
                map_value = np.mean(precision_values)
            else:
                # If no correct answer is found, set MAP to 0
                map_value = 0
            return map_value, [map_value]
        elif isinstance(data, list):
            # Calculate MAP for a list of tuples
            map_values = []
            for item in data:
                map_value, _ = MetricsCalculator2.map(item)
                map_values.append(map_value)
            # Calculate average MAP
            average_map = np.mean(map_values)
            return average_map, map_values
        else:
            # Raise an error if input data is not a tuple or a list of tuples
            raise ValueError("Invalid input data")