import numpy as np
from gensim import matutils

class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        return np.dot(vector_1, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        return [np.dot(vector_1, vector) / (np.linalg.norm(vector_1) * np.linalg.norm(vector)) for vector in vectors_all]

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        return np.mean([np.dot(vector_1, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2)) for vector_1, vector_2 in zip(vector_list_1, vector_list_2)])

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        return {key: np.log(total_num + 1) / (np.log(count + 1) + 1) for key, count in number_dict.items()}