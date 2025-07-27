class VectorUtil:
    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :return: float, Contains cosine similarity between `vector_1` and `vector_2`
        """
        # Normalize both vectors to unit vectors
        vector_1 = matutils.unitvec(array(vector_1))
        vector_2 = matutils.unitvec(array(vector_2))
        
        # Compute and return the dot product, which is the cosine similarity for unit vectors
        return dot(vector_1, vector_2)

    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :return: numpy.ndarray, Contains cosine similarities between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        """
        # Normalize the input vector to a unit vector
        vector_1 = matutils.unitvec(array(vector_1))
        
        # Normalize all vectors in vectors_all to unit vectors
        vectors_all = matutils.unitvec(array(vectors_all))
        
        # Compute the dot product between vector_1 and each vector in vectors_all
        return np.dot(vectors_all, vector_1)

    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :return: float, Similarities between vector_list_1 and vector_list_2.
        """
        # Convert lists of vectors to arrays
        vector_list_1 = np.array(vector_list_1)
        vector_list_2 = np.array(vector_list_2)
        
        # Compute mean vectors for each list
        mean_vector_1 = np.mean(vector_list_1, axis=0)
        mean_vector_2 = np.mean(vector_list_2, axis=0)
        
        # Return the cosine similarity between the mean vectors
        return VectorUtil.similarity(mean_vector_1, mean_vector_2)

    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :return: dict
        """
        # Initialize an empty dictionary to store IDF weights
        idf_weights = {}
        
        # Calculate IDF weight for each term in number_dict
        for term, count in number_dict.items():
            # Compute IDF using the formula: log((total_num + 1) / (count + 1))
            idf_weights[term] = np.log((total_num + 1) / (count + 1))
        
        # Return the dictionary of IDF weights
        return idf_weights