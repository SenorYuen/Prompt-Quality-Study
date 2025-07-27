from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    # Method to calculate the mean of a given data set
    def mean(self, data):
        # Check if the data list is empty
        if not data:
            return None
        
        # Calculate the sum of all elements in the data list
        total = sum(data)
        
        # Calculate the mean by dividing the sum by the number of elements
        mean_value = total / len(data)
        
        # Return the mean value rounded to two decimal places
        return round(mean_value, 2)

    # Method to calculate the median of a given data set
    def median(self, data):
        # Check if the data list is empty
        if not data:
            return None
        
        # Sort the data list in ascending order
        sorted_data = sorted(data)
        
        # Get the length of the data list
        n = len(sorted_data)
        
        # If the length is even, calculate the median as the average of the two middle numbers
        if n % 2 == 0:
            median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        # If the length is odd, calculate the median as the middle number
        else:
            median_value = sorted_data[n // 2]
        
        # Return the median value rounded to two decimal places
        return round(median_value, 2)

    # Method to calculate the mode of a given data set
    def mode(self, data):
        # Check if the data list is empty
        if not data:
            return None
        
        # Use the Counter class to count the frequency of each element in the data list
        frequency = Counter(data)
        
        # Find the maximum frequency
        max_frequency = max(frequency.values())
        
        # Get the elements with the maximum frequency
        modes = [num for num, freq in frequency.items() if freq == max_frequency]
        
        # Return the modes
        return modes