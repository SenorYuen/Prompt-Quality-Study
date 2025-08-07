import numpy as np

class KappaCalculator:
    @staticmethod
    def kappa(testData, k):
        testData = np.array(testData)
        num_raters = testData.shape[0]
        num_items = testData.shape[1]

        # Calculate the proportion of agreement
        p0 = np.sum(np.diag(testData)) / np.sum(testData)

        # Calculate the expected proportion of agreement by chance
        pe = np.sum(np.dot(np.sum(testData, axis=0), np.sum(testData, axis=1))) / (np.sum(testData) ** 2)

        # Calculate kappa
        kappa_value = (p0 - pe) / (1 - pe)
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        testData = np.array(testData)

        # Calculate proportion of ratings in each category
        p = np.sum(testData, axis=0) / (N * n)

        # Calculate the degree of agreement for each subject
        P = (np.sum(testData ** 2, axis=1) - n) / (n * (n - 1))

        # Calculate the mean of P
        Pbar = np.mean(P)

        # Calculate the mean of p squared
        PbarE = np.sum(p ** 2)

        # Calculate Fleiss' kappa
        kappa_value = (Pbar - PbarE) / (1 - PbarE)
        return kappa_value