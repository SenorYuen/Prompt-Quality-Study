# This is a class for performing data statistics, supporting to get the sum, minimum, maximum, variance, standard deviation, and correlation of a given dataset.

import numpy as np

class DataStatistics2:
    # Initialize Data List
    def __init__(self, data):
        # Check if input data is a list
        if not isinstance(data, list):
            raise TypeError("Input data must be a list")
        # Check if list is not empty
        if len(data) == 0:
            raise ValueError("Input list cannot be empty")
        # Check if all elements in the list are numbers
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All elements in the list must be numbers")
        self.data = np.array(data)  # Convert list to numpy array for efficient calculations

    # Calculate the sum of data
    def get_sum(self):
        # Use numpy's sum function to calculate the sum of the data
        return np.sum(self.data)

    # Calculate the minimum value in the data
    def get_min(self):
        # Use numpy's min function to find the minimum value in the data
        return np.min(self.data)

    # Calculate the maximum value in the data
    def get_max(self):
        # Use numpy's max function to find the maximum value in the data
        return np.max(self.data)

    # Calculate variance, accurate to two digits after the Decimal separator
    def get_variance(self):
        # Use numpy's var function to calculate the variance of the data
        return round(np.var(self.data), 2)

    # Calculate standard deviation, accurate to two digits after the Decimal separator
    def get_std_deviation(self):
        # Use numpy's std function to calculate the standard deviation of the data
        return round(np.std(self.data), 2)

    # Calculate correlation
    def get_correlation(self):
        # Since correlation is typically calculated between two datasets, 
        # we'll calculate the correlation of the data with itself
        # This will give us a correlation coefficient of 1.0
        # For a more meaningful correlation calculation, you would need two separate datasets
        return np.corrcoef(self.data, self.data)[0, 1]