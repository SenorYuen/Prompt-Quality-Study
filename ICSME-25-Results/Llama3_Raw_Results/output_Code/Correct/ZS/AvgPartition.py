class AvgPartition:
    def __init__(self, lst, limit):
        # Check if the number of partitions is greater than 0
        if limit <= 0:
            raise ValueError("Number of partitions must be greater than 0")
        # Initialize the list and the number of partitions
        self.lst = lst
        self.limit = limit

    def setNum(self):
        # Calculate the size of each block
        block_size = len(self.lst) // self.limit
        # Calculate the remainder of the division
        remainder = len(self.lst) % self.limit
        # Return the size of each block and the remainder of the division
        return block_size, remainder


    def get(self, index):
        # Check if the index is within the valid range
        if index < 0 or index >= self.limit:
            raise IndexError("Index out of range")
        
        # Calculate the size of each block and the remainder of the division
        block_size, remainder = self.setNum()
        
        # Calculate the start position of the block
        start = index * block_size + min(index, remainder)
        
        # Calculate the end position of the block
        end = (index + 1) * block_size + min(index + 1, remainder)
        
        # Return the corresponding block
        return self.lst[start:end]

# Example usage:
avg_partition = AvgPartition([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print(avg_partition.get(0))  # Output: [1, 2, 3]
print(avg_partition.get(1))  # Output: [4, 5, 6]
print(avg_partition.get(2))  # Output: [7, 8, 9]