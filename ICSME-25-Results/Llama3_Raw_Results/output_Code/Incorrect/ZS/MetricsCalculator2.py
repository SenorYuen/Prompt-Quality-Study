import numpy as np

class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        # Check if input data is a list of lists
        if isinstance(data[0], list):
            # Initialize list to store MRR for each sublist
            mrr_list = []
            # Iterate over each sublist
            for sublist in data:
                # Find the index of the first relevant item (assuming relevant items are marked as 1)
                relevant_index = next((i for i, x in enumerate(sublist) if x == 1), None)
                # If a relevant item is found, calculate the reciprocal rank
                if relevant_index is not None:
                    mrr_list.append(1 / (relevant_index + 1))
                # If no relevant item is found, set the reciprocal rank to 0
                else:
                    mrr_list.append(0)
            # Calculate the mean of the reciprocal ranks
            mrr_value = np.mean(mrr_list)
            return mrr_value, mrr_list
        # If input data is a single list
        else:
            # Find the index of the first relevant item (assuming relevant items are marked as 1)
            relevant_index = next((i for i, x in enumerate(data) if x == 1), None)
            # If a relevant item is found, calculate the reciprocal rank
            if relevant_index is not None:
                mrr_value = 1 / (relevant_index + 1)
            # If no relevant item is found, set the reciprocal rank to 0
            else:
                mrr_value = 0
            return mrr_value, [mrr_value]

    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """
        # Check if input data is a list of lists
        if isinstance(data[0], list):
            # Initialize list to store AP for each sublist
            ap_list = []
            # Iterate over each sublist
            for sublist in data:
                # Initialize variables to calculate precision and recall
                relevant_count = 0
                precision_sum = 0
                # Iterate over each item in the sublist
                for i, item in enumerate(sublist):
                    # If the item is relevant (assuming relevant items are marked as 1)
                    if item == 1:
                        relevant_count += 1
                        # Calculate the precision at this point
                        precision = relevant_count / (i + 1)
                        precision_sum += precision
                # If there are relevant items, calculate the average precision
                if relevant_count > 0:
                    ap = precision_sum / relevant_count
                # If there are no relevant items, set the average precision to 0
                else:
                    ap = 0
                ap_list.append(ap)
            # Calculate the mean of the average precisions
            map_value = np.mean(ap_list)
            return map_value, ap_list
        # If input data is a single list
        else:
            # Initialize variables to calculate precision and recall
            relevant_count = 0
            precision_sum = 0
            # Iterate over each item in the list
            for i, item in enumerate(data):
                # If the item is relevant (assuming relevant items are marked as 1)
                if item == 1:
                    relevant_count += 1
                    # Calculate the precision at this point
                    precision = relevant_count / (i + 1)
                    precision_sum += precision
            # If there are relevant items, calculate the average precision
            if relevant_count > 0:
                map_value = precision_sum / relevant_count
            # If there are no relevant items, set the average precision to 0
            else:
                map_value = 0
            return map_value, [map_value]