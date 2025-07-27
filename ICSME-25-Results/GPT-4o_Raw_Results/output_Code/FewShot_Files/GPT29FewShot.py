from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        # Calculate the mean by dividing the sum of data by the number of data points
        mean_value = sum(data) / len(data)
        # Return the result rounded to two decimal places
        return round(mean_value, 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        # Sort the data list
        sorted_data = sorted(data)
        n = len(sorted_data)
        # Calculate the median based on whether the number of data points is odd or even
        if n % 2 == 1:
            median_value = sorted_data[n // 2]
        else:
            median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        # Return the result rounded to two decimal places
        return round(median_value, 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        # Use Counter to count the frequency of each element in the data list
        data_counter = Counter(data)
        # Find the maximum frequency
        max_count = max(data_counter.values())
        # Find all elements that have the maximum frequency
        mode_values = [k for k, v in data_counter.items() if v == max_count]
        # Return the list of mode values
        return mode_values