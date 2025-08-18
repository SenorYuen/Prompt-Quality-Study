'''
# The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.

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


    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        """

'''

import numpy as np


class MetricsCalculator2:
    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        if type(data) != list and type(data) != tuple:
            raise Exception("the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

        if len(data) == 0:
            return 0.0, [0.0]
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)
                mr_np = sub_list * ranking_array

                mr = 0.0
                for team in mr_np:
                    if team > 0:
                        mr = team
                        break
                return mr, [mr]

        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)

                if total_num == 0:
                    mr = 0.0
                else:
                    ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)
                    mr_np = sub_list * ranking_array

                    mr = 0.0
                    for team in mr_np:
                        if team > 0:
                            mr = team
                            break

                separate_result.append(mr)
            return np.mean(separate_result), separate_result

    @staticmethod
    def map(data):
        if type(data) != list and type(data) != tuple:
            raise Exception("the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

        if len(data) == 0:
            return 0.0, [0.0]
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)

                right_ranking_list = []
                count = 1
                for t in sub_list:
                    if t == 0:
                        right_ranking_list.append(0)
                    else:
                        right_ranking_list.append(count)
                        count += 1

                ap = np.sum(np.array(right_ranking_list) * ranking_array) / total_num
                return ap, [ap]

        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)

                if total_num == 0:
                    ap = 0.0
                else:
                    ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)

                    right_ranking_list = []
                    count = 1
                    for t in sub_list:
                        if t == 0:
                            right_ranking_list.append(0)
                        else:
                            right_ranking_list.append(count)
                            count += 1

                    ap = np.sum(np.array(right_ranking_list) * ranking_array) / total_num

                separate_result.append(ap)
            return np.mean(separate_result), separate_result

