import numpy as np

class KappaCalculator:

    @staticmethod
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :return: float, the cohens kappa value of the matrix
        """
        # Calculate the observed agreement
        po = np.sum(np.diag(testData)) / np.sum(testData)
        
        # Calculate the expected agreement
        pe = np.sum(np.sum(testData, axis=0) * np.sum(testData, axis=1)) / (np.sum(testData) ** 2)
        
        # Calculate Cohen's kappa
        kappa = (po - pe) / (1 - pe)
        
        return kappa

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :return: float, fleiss kappa value
        """
        # Calculate the proportion of raters that assigned each category to each item
        proportions = np.sum(testData, axis=0) / (N * n)
        
        # Calculate the proportion of items that were assigned to each category
        item_proportions = np.sum(testData, axis=1) / n
        
        # Calculate the expected proportion of agreement for each category
        expected_proportions = np.sum(item_proportions ** 2)
        
        # Calculate the observed proportion of agreement for each category
        observed_proportions = np.sum(proportions ** 2)
        
        # Calculate Fleiss' kappa
        kappa = (observed_proportions - expected_proportions) / (1 - expected_proportions)
        
        return kappa