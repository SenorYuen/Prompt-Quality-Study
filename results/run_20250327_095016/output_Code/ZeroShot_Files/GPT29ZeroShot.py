from collections import Counter

class DataStatistics:
    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :return: float, the mean value
        """
        if not data:
            return None
        # Calculate the mean by dividing the sum of the data by the number of data points
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :return: float, the median value
        """
        if not data:
            return None
        # Sort the data to find the median
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        # Check if the number of data points is odd or even
        if n % 2 == 0:
            # If even, median is the average of the two middle numbers
            median_value = (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            # If odd, median is the middle number
            median_value = sorted_data[mid]

        return round(median_value, 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :return: float, the mode
        """
        if not data:
            return None
        # Use Counter to count the frequency of each element in the data
        data_count = Counter(data)
        # Find the maximum frequency
        max_count = max(data_count.values())
        # Find the element(s) with the maximum frequency
        mode_values = [k for k, v in data_count.items() if v == max_count]

        # If there's a tie for the mode, return the first one encountered
        return mode_values[0] if mode_values else None