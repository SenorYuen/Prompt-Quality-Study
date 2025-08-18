'''
# This is a class used to process binary data, which includes functions such as clearing non 0 or 1 characters, counting binary string information, and converting to corresponding strings based on different encoding methods.

class BinaryDataProcessor:
    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        """

    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non 0 or 1 characters.
        """

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
'''

class BinaryDataProcessor:
    def __init__(self, binary_string):
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))

    def calculate_binary_info(self):
        zeroes_count = self.binary_string.count('0')
        ones_count = self.binary_string.count('1')
        total_length = len(self.binary_string)

        zeroes_percentage = (zeroes_count / total_length)
        ones_percentage = (ones_count / total_length)

        return {
            'Zeroes': zeroes_percentage,
            'Ones': ones_percentage,
            'Bit length': total_length
        }

    def convert_to_ascii(self):
        byte_array = bytearray()
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            decimal = int(byte, 2)
            byte_array.append(decimal)

        return byte_array.decode('ascii')

    def convert_to_utf8(self):
        byte_array = bytearray()
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            decimal = int(byte, 2)
            byte_array.append(decimal)

        return byte_array.decode('utf-8')


