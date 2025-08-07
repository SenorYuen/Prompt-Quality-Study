import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """

    @staticmethod
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        # Convert testData to numpy array for easier manipulation
        testData = np.array(testData)
        
        # Calculate the total number of observations
        n = np.sum(testData)
        
        # Calculate the observed agreement (Po)
        Po = np.trace(testData) / n
        
        # Calculate the expected agreement (Pe)
        sum_rows = np.sum(testData, axis=1)
        sum_cols = np.sum(testData, axis=0)
        Pe = np.sum(sum_rows * sum_cols) / (n ** 2)
        
        # Calculate Cohen's Kappa
        kappa_value = (Po - Pe) / (1 - Pe)
        
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fleiss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                              [0, 2, 6, 4, 2],
        >>>                              [0, 0, 3, 5, 6],
        >>>                              [0, 3, 9, 2, 0],
        >>>                              [2, 2, 8, 1, 1],
        >>>                              [7, 7, 0, 0, 0],
        >>>                              [3, 2, 6, 3, 0],
        >>>                              [2, 5, 3, 2, 2],
        >>>                              [6, 5, 2, 1, 0],
        >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        # Convert testData to numpy array for easier manipulation
        testData = np.array(testData)
        
        # Calculate the proportion of all assignments to each category
        p = np.sum(testData, axis=0) / (N * n)
        
        # Calculate the extent to which raters agree for each item
        Pj = (np.sum(testData * (testData - 1), axis=1) / (n * (n - 1)))
        
        # Calculate the mean of Pj
        P_mean = np.mean(Pj)
        
        # Calculate the mean of p squared
        P_e = np.sum(p ** 2)
        
        # Calculate Fleiss' Kappa
        kappa_value = (P_mean - P_e) / (1 - P_e)
        
        return kappa_value