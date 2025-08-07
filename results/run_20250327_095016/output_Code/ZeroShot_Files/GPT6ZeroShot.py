class AvgPartition:
    def __init__(self, lst, limit):
        """
        Initialize the class with the given list and the number of partitions.
        Check if the number of partitions is greater than 0.
        """
        if limit <= 0:
            raise ValueError("Number of partitions must be greater than 0.")
        self.lst = lst
        self.limit = limit

    def setNum(self):
        """
        Calculate the size of each block and the remainder of the division.
        :return: the size of each block and the remainder of the division, tuple.
        """
        n = len(self.lst)
        block_size = n // self.limit  # Integer division to get the base size of each block
        remainder = n % self.limit    # Remainder to distribute among the first few blocks
        return block_size, remainder

    def get(self, index):
        """
        Calculate the size of each block and the remainder of the division.
        Calculate the corresponding start and end positions based on the index of the partition.
        :return: the corresponding block, list.
        """
        if index < 0 or index >= self.limit:
            raise IndexError("Index out of range for the number of partitions.")
        
        block_size, remainder = self.setNum()

        # Calculate the start position
        start = index * block_size + min(index, remainder)
        # Calculate the end position
        end = start + block_size + (1 if index < remainder else 0)

        return self.lst[start:end]