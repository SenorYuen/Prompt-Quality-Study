from collections import Counter

class DataStatistics:
    
    def mean(self, data):
        return round(sum(data) / len(data), 2)

    def median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
        else:
            return round(sorted_data[mid], 2)

    def mode(self, data):
        data_count = Counter(data)
        max_count = max(data_count.values())
        modes = [key for key, value in data_count.items() if value == max_count]
        return modes