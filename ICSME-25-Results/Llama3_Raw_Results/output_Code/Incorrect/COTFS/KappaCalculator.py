import numpy as np

class KappaCalculator:
    @staticmethod
    def kappa(testData, k):
        # Calculate the Cohen's kappa value of a k-dimensional matrix
        data = np.array(testData)
        po = np.trace(data) / np.sum(data)
        pe = np.sum(np.multiply(np.sum(data, axis=0), np.sum(data, axis=1))) / np.sum(data)**2
        kappa = (po - pe) / (1 - pe)
        return kappa

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        # Calculate the Fleiss kappa value of an N * k matrix
        data = np.array(testData)
        p_j = np.sum(data, axis=0) / (N * n)
        p_e = np.sum(np.square(p_j))
        p_i = np.sum(np.square(data), axis=1) / n**2
        p_o = np.sum(p_i) / N
        kappa = (p_o - p_e) / (1 - p_e)
        return kappa