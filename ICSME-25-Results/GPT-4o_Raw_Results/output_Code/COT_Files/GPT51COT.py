import numpy as np

class KappaCalculator:
    @staticmethod
    def kappa(testData, k):
        matrix = np.array(testData)
        p_o = np.sum(np.diag(matrix)) / np.sum(matrix)
        p_e = np.sum(np.sum(matrix, axis=0) * np.sum(matrix, axis=1)) / (np.sum(matrix) ** 2)
        return (p_o - p_e) / (1 - p_e)

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        matrix = np.array(testData)
        p = np.sum(matrix, axis=0) / (N * n)
        P = (np.sum(matrix**2, axis=1) - n) / (n * (n - 1))
        P_bar = np.mean(P)
        P_e_bar = np.sum(p**2)
        return (P_bar - P_e_bar) / (1 - P_e_bar)