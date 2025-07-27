import numpy as np

class KappaCalculator:
    @staticmethod
    def kappa(testData, k):
        # Calculate the Cohen's kappa value of a k-dimensional matrix
        # testData: k-dimensional matrix
        # k: Matrix dimension
        # Return the cohen's kappa value of the matrix as float
        
        # Calculate the observed agreement (Po)
        Po = 0
        for i in range(k):
            Po += testData[i][i]
        Po /= sum(sum(row) for row in testData)
        
        # Calculate the expected agreement (Pe)
        Pe = 0
        row_sums = [sum(row) for row in testData]
        col_sums = [sum(col) for col in zip(*testData)]
        total = sum(row_sums)
        for i in range(k):
            Pe += (row_sums[i] * col_sums[i]) / (total ** 2)
        
        # Calculate the Cohen's kappa value
        kappa = (Po - Pe) / (1 - Pe)
        return kappa

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        # Calculate the Fleiss kappa value of an N * k matrix
        # testData: Input data matrix, N * k
        # N: Number of samples
        # k: Number of categories
        # n: Number of raters
        # Return Fleiss kappa value as float
        
        # Calculate the proportion of raters who assigned each category to each item
        proportions = np.array(testData) / n
        
        # Calculate the average proportion of raters who assigned each category
        average_proportions = np.mean(proportions, axis=0)
        
        # Calculate the observed agreement (P)
        P = (np.sum(np.square(proportions), axis=1) - 1) / (n * (n - 1))
        P_bar = np.mean(P)
        
        # Calculate the expected agreement (Pe)
        Pe = np.sum(np.square(average_proportions))
        
        # Calculate the Fleiss kappa value
        kappa = (P_bar - Pe) / (1 - Pe)
        return kappa