'''
# The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.

import numpy as np
from gensim import matutils
from numpy import dot, array

class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and `vector_2`
        """


    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        """


    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        """


    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :return: dict
        """

'''

import numpy as np
from gensim import matutils
from numpy import dot, array


class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        norm = np.linalg.norm(vector_1)
        all_norms = np.linalg.norm(vectors_all, axis=1)
        dot_products = dot(vectors_all, vector_1)
        similarities = dot_products / (norm * all_norms)
        return similarities

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        if not (len(vector_list_1) and len(vector_list_2)):
            raise ZeroDivisionError('At least one of the passed list is empty.')

        return dot(matutils.unitvec(array(vector_list_1).mean(axis=0)),
                   matutils.unitvec(array(vector_list_2).mean(axis=0)))

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        index_2_key_map = {}

        index = 0

        count_list = []
        for key, count in number_dict.items():
            index_2_key_map[index] = key
            count_list.append(count)
            index = index + 1

        a = np.array(count_list)
        ## smooth, in case the divide by zero error
        a = np.log((total_num + 1) / (a + 1))
        result = {}

        for index, w in enumerate(a):
            key = index_2_key_map[index]
            result[key] = w

        return result
