class AvgPartition:
    def __init__(self, lst, limit):
        # Check if the number of partitions is greater than 0
        if limit <= 0:
            raise ValueError("Number of partitions must be greater than 0")
        self.lst = lst
        self.limit = limit

    def setNum(self):
        # Calculate the size of each block and the remainder of the division
        block_size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return (block_size, remainder)

    def get(self, index):
        # Calculate the size of each block and the remainder of the division
        block_size, remainder = self.setNum()
        
        # Calculate the start and end positions based on the index of the partition
        start = index * block_size + min(index, remainder)
        end = (index + 1) * block_size + min(index + 1, remainder)
        
        # Return the corresponding block as list
        return self.lst[start:end]