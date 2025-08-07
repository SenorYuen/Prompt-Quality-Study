import numpy as np

class KappaCalculator:

    @staticmethod
    def kappa(testData, k):
        """
        Calculate the Cohen's kappa value of a k-dimensional matrix
        :param testData: 2D list or array, where each row is a pair of ratings from two raters
        :param k: int, the number of categories
        :return: float, the Cohen's kappa value of the matrix
        """
        # Convert testData to a numpy array for easier manipulation
        testData = np.array(testData)
        
        # Calculate the observed agreement
        total_agreements = np.sum(testData[:, 0] == testData[:, 1])
        total_pairs = len(testData)
        p_o = total_agreements / total_pairs
        
        # Calculate the expected agreement
        p_e = 0
        for i in range(k):
            p_i = np.sum(testData[:, 0] == i) / total_pairs
            p_j = np.sum(testData[:, 1] == i) / total_pairs
            p_e += p_i * p_j
        
        # Calculate Cohen's kappa
        kappa_value = (p_o - p_e) / (1 - p_e)
        
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the Fleiss' kappa value of an N * k matrix
        :param testData: 2D list or array (N*k), where each row represents the count of ratings for each category
        :param N: int, number of subjects
        :param k: int, number of categories
        :param n: int, number of ratings per subject
        :return: float, the Fleiss' kappa value
        """
        # Convert testData to a numpy array for easier manipulation
        testData = np.array(testData)
        
        # Calculate the proportion of all assignments to each category
        p_j = np.sum(testData, axis=0) / (N * n)
        
        # Calculate the agreement for each subject
        P_i = (np.sum(testData**2, axis=1) - n) / (n * (n - 1))
        
        # Calculate the mean of P_i
        P_bar = np.mean(P_i)
        
        # Calculate the mean of p_j squared
        P_e_bar = np.sum(p_j**2)
        
        # Calculate Fleiss' kappa
        kappa_value = (P_bar - P_e_bar) / (1 - P_e_bar)
        
        return kappa_value