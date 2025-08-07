import numpy as np


class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        Compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        
        :param data: A list of lists, where each sublist contains binary relevance scores (1 for relevant, 0 for non-relevant).
        :return: A tuple containing the MRR score and a list of reciprocal ranks for each sublist.
        """
        reciprocal_ranks = []
        
        for query_results in data:
            # Find the rank of the first relevant item (1)
            try:
                rank = query_results.index(1) + 1
                reciprocal_ranks.append(1 / rank)
            except ValueError:
                # If there is no relevant item, the reciprocal rank is 0
                reciprocal_ranks.append(0)

        # Calculate the mean reciprocal rank
        mean_reciprocal_rank = np.mean(reciprocal_ranks)
        return mean_reciprocal_rank, reciprocal_ranks

    @staticmethod
    def map(data):
        """
        Compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        
        :param data: A list of lists, where each sublist contains binary relevance scores (1 for relevant, 0 for non-relevant).
        :return: A tuple containing the MAP score and a list of average precisions for each sublist.
        """
        average_precisions = []

        for query_results in data:
            num_relevant = 0
            precision_sum = 0.0
            
            for i, score in enumerate(query_results):
                if score == 1:
                    num_relevant += 1
                    precision_at_i = num_relevant / (i + 1)
                    precision_sum += precision_at_i
            
            # Calculate average precision for the current query
            if num_relevant > 0:
                average_precision = precision_sum / num_relevant
            else:
                average_precision = 0.0

            average_precisions.append(average_precision)

        # Calculate the mean average precision
        mean_average_precision = np.mean(average_precisions)
        return mean_average_precision, average_precisions