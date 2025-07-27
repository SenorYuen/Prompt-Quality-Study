import numpy as np
from gensim import matutils
from numpy import dot, array

class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        return dot(matutils.unitvec(array(vector_1)), matutils.unitvec(array(vector_2)))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        return [dot(matutils.unitvec(array(vector_1)), matutils.unitvec(array(vector_2))) for vector_2 in vectors_all]

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        mean_vector_1 = matutils.unitvec(array(vector_list_1).mean(axis=0))
        mean_vector_2 = matutils.unitvec(array(vector_list_2).mean(axis=0))
        return dot(mean_vector_1, mean_vector_2)

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        return {key: np.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}