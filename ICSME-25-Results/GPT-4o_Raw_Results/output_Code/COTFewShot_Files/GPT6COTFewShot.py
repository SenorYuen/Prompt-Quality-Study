class AvgPartition:
    def __init__(self, lst, limit):
        if limit <= 0:
            raise ValueError("Number of partitions must be greater than 0.")
        self.lst = lst
        self.limit = limit

    def setNum(self):
        length = len(self.lst)
        size = length // self.limit
        remainder = length % self.limit
        return size, remainder

    def get(self, index):
        size, remainder = self.setNum()
        start = index * size + min(index, remainder)
        end = start + size + (1 if index < remainder else 0)
        return self.lst[start:end]