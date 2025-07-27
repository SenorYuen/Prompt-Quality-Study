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
        # Calculate the total number of observations
        total_observations = sum(sum(row) for row in testData)
        
        # Calculate the observed agreement
        observed_agreement = sum(testData[i][i] for i in range(k)) / total_observations
        
        # Calculate the expected agreement
        expected_agreement = sum((sum(testData[i]) / total_observations) * (sum(testData[j]) / total_observations) for i in range(k) for j in range(k)) / k
        
        # Calculate Cohen's kappa
        kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        
        return kappa

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
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
        # Calculate the total number of observations
        total_observations = N * n
        
        # Calculate the observed agreement
        observed_agreement = 0
        for i in range(N):
            max_category_count = max(testData[i])
            observed_agreement += (max_category_count / n) ** 2
        
        observed_agreement = (observed_agreement - 1) / (N - 1)
        
        # Calculate the expected agreement
        expected_agreement = 0
        for j in range(k):
            category_count = sum(testData[i][j] for i in range(N))
            expected_agreement += (category_count / total_observations) ** 2
        
        # Calculate Fleiss' kappa
        kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        
        return kappa