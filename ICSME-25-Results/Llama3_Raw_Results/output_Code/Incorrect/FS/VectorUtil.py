import numpy as np
from gensim import matutils
from numpy import dot, array

class VectorUtil:
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        # Compute the cosine similarity between one vector and another vector
        # Using the dot product and magnitude of vectors
        return dot(vector_1, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2))

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        # Compute cosine similarities between one vector and a set of other vectors
        # Using list comprehension to calculate similarity for each vector
        return [VectorUtil.similarity(vector_1, vector) for vector in vectors_all]

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        # Compute cosine similarity between two sets of vectors
        # Calculate the average of the cosine similarities of the vectors
        similarities = []
        for vector1 in vector_list_1:
            for vector2 in vector_list_2:
                similarities.append(VectorUtil.similarity(vector1, vector2))
        return np.mean(similarities)

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        # Calculate log(total_num+1/count+1) for each count in number_dict
        # Using dictionary comprehension to calculate IDF weights
        return {key: np.log(total_num + 1) - np.log(value + 1) for key, value in number_dict.items()}