'''
# This is a class that partitions the given list into different blocks by specifying the number of partitions, with each block having a uniformly distributed length.

class AvgPartition:
    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions, and check if the number of partitions is greater than 0.
        """

    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        """


    def get(self, index):
        """
        calculate the size of each block and the remainder of the division, and calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        """
'''

class AvgPartition:
    def __init__(self, lst, limit):
        self.lst = lst
        self.limit = limit

    def setNum(self):
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return size, remainder

        
    def get(self, index):
        size, remainder = self.setNum()
        start = index * size + min(index, remainder)
        end = start + size
        if index + 1 <= remainder:
            end += 1
        return self.lst[start:end]