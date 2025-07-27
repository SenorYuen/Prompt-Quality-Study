class BinaryDataProcessor:
    """
    This is a class used to process binary data, which includes functions such as clearing non 0 or 1 characters,
    counting binary string information, and converting to corresponding strings based on different encoding methods.
    """

    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non 0 or 1 characters.
        """
        # Use a list comprehension to filter out non '0' or '1' characters
        self.binary_string = ''.join([char for char in self.binary_string if char in '01'])

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        # Calculate the total length of the binary string
        total_length = len(self.binary_string)
        # Calculate the count of '0's and '1's
        count_zeroes = self.binary_string.count('0')
        count_ones = self.binary_string.count('1')
        # Calculate the percentage of '0's and '1's
        percentage_zeroes = count_zeroes / total_length
        percentage_ones = count_ones / total_length
        # Return the calculated information as a dictionary
        return {
            'Zeroes': percentage_zeroes,
            'Ones': percentage_ones,
            'Bit length': total_length
        }

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        # Split the binary string into chunks of 8 bits (1 byte)
        chars = [self.binary_string[i:i+8] for i in range(0, len(self.binary_string), 8)]
        # Convert each byte to an ASCII character and join them into a string
        ascii_string = ''.join([chr(int(char, 2)) for char in chars])
        return ascii_string

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        # Split the binary string into chunks of 8 bits (1 byte)
        chars = [self.binary_string[i:i+8] for i in range(0, len(self.binary_string), 8)]
        # Convert each byte to an ASCII character and join them into a string
        utf8_string = ''.join([chr(int(char, 2)) for char in chars])
        return utf8_string