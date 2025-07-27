from collections import Counter
import statistics

class DataStatistics:
    def mean(self, data):
        return round(sum(data) / len(data), 2)

    def median(self, data):
        sorted_data = sorted(data)
        return round(statistics.median(sorted_data), 2)

    def mode(self, data):
        counter = Counter(data)
        max_count = max(counter.values())
        modes = [num for num, count in counter.items() if count == max_count]
        return modes