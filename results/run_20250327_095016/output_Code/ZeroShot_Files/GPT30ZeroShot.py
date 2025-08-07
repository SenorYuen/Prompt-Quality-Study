import numpy as np

class DataStatistics2:
    def __init__(self, data):
        """
        Initialize Data List
        """
        self.data = np.array(data)  # Convert input data to a numpy array for easy calculations

    def get_sum(self):
        """
        Calculate the sum of data
        :return:float
        """
        return np.sum(self.data)  # Use numpy's sum function to calculate the sum

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        """
        return np.min(self.data)  # Use numpy's min function to find the minimum value

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        """
        return np.max(self.data)  # Use numpy's max function to find the maximum value

    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        """
        return round(np.var(self.data), 2)  # Use numpy's var function and round to 2 decimal places

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        """
        return round(np.std(self.data), 2)  # Use numpy's std function and round to 2 decimal places

    def get_correlation(self, other_data):
        """
        Calculate correlation with another dataset
        :param other_data: list or array-like object
        :return:float
        """
        other_data = np.array(other_data)  # Convert the other_data to a numpy array
        if len(self.data) != len(other_data):
            raise ValueError("Datasets must have the same length")  # Ensure both datasets are of the same length
        correlation_matrix = np.corrcoef(self.data, other_data)  # Calculate the correlation matrix
        return correlation_matrix[0, 1]  # Return the correlation coefficient between the two datasets