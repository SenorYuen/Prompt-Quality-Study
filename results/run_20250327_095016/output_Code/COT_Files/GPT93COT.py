import numpy as np
from gensim import matutils
from numpy import dot, array

class VectorUtil:

    @staticmethod
    def similarity(vector_1: np.ndarray, vector_2: np.ndarray) -> float:
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))

    @staticmethod
    def cosine_similarities(vector_1: np.ndarray, vectors_all: list) -> np.ndarray:
        vector_1_norm = matutils.unitvec(vector_1)
        return np.array([dot(vector_1_norm, matutils.unitvec(vector)) for vector in vectors_all])

    @staticmethod
    def n_similarity(vector_list_1: list, vector_list_2: list) -> float:
        mean_vector_1 = matutils.unitvec(array(vector_list_1).mean(axis=0))
        mean_vector_2 = matutils.unitvec(array(vector_list_2).mean(axis=0))
        return dot(mean_vector_1, mean_vector_2)

    @staticmethod
    def compute_idf_weight_dict(total_num: int, number_dict: dict) -> dict:
        return {key: np.log((total_num + 1) / (count + 1)) for key, count in number_dict.items()}