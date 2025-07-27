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
        # Ensure vectors are numpy arrays
        vector_1 = np.array(vector_1)
        vector_2 = np.array(vector_2)
        
        # Calculate cosine similarity using gensim's matutils
        similarity = matutils.cosine_similarities([vector_1], [vector_2])
        
        # Return the similarity
        return similarity[0][0]

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        """
        # Ensure vector_1 is a numpy array and vectors_all is a 2D numpy array
        vector_1 = np.array(vector_1)
        vectors_all = np.array(vectors_all)
        
        # Calculate cosine similarities using gensim's matutils
        similarities = matutils.cosine_similarities([vector_1], vectors_all)
        
        # Return the similarities
        return similarities[0]

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        """
        # Ensure both lists are numpy arrays
        vector_list_1 = np.array(vector_list_1)
        vector_list_2 = np.array(vector_list_2)
        
        # Calculate cosine similarities using gensim's matutils
        similarities = matutils.cossim(vector_list_1, vector_list_2)
        
        # Return the similarities
        return similarities

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :return: dict
        """
        # Initialize an empty dictionary to store IDF weights
        idf_weight_dict = {}
        
        # Iterate over each key-value pair in number_dict
        for key, count in number_dict.items():
            # Calculate IDF weight
            idf_weight = np.log((total_num + 1) / (count + 1))
            
            # Store IDF weight in idf_weight_dict
            idf_weight_dict[key] = idf_weight
        
        # Return the idf_weight_dict
        return idf_weight_dict