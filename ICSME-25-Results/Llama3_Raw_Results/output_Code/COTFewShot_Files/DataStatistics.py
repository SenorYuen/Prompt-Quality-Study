from collections import Counter
import statistics

class DataStatistics:
    def mean(self, data):
        return round(sum(data) / len(data), 2)

    def median(self, data):
        return round(statistics.median(data), 2)

    def mode(self, data):
        mode_data = Counter(data)
        max_count = max(mode_data.values())
        modes = [num for num, count in mode_data.items() if count == max_count]
        return modes