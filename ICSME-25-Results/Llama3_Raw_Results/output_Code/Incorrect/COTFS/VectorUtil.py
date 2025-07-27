import numpy as np
from gensim import matutils
from numpy import dot, array

class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        similarities = []
        for vector_2 in vectors_all:
            similarity = dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))
            similarities.append(similarity)
        return np.array(similarities)

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        return np.mean([VectorUtil.similarity(vector_1, vector_2) for vector_1, vector_2 in zip(vector_list_1, vector_list_2)])

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        idf_weight_dict = {}
        for key, count in number_dict.items():
            idf_weight = np.log(total_num + 1) - np.log(count + 1)
            idf_weight_dict[key] = idf_weight
        return idf_weight_dict