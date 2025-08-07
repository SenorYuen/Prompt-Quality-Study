class BinaryDataProcessor:
    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        """
        self.original_string = binary_string
        self.binary_string = self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non 0 or 1 characters.
        """
        # Use a list comprehension to filter out non-binary characters
        return ''.join([char for char in self.original_string if char in '01'])

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        """
        length = len(self.binary_string)
        if length == 0:
            return {'length': 0, 'percentage_0': 0, 'percentage_1': 0}
        
        count_0 = self.binary_string.count('0')
        count_1 = self.binary_string.count('1')
        percentage_0 = (count_0 / length) * 100
        percentage_1 = (count_1 / length) * 100
        
        return {'length': length, 'percentage_0': percentage_0, 'percentage_1': percentage_1}

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        """
        ascii_string = ''
        # Process the binary string in chunks of 8 bits
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            if len(byte) == 8:
                ascii_string += chr(int(byte, 2))
        return ascii_string

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        """
        utf8_string = ''
        # Process the binary string in chunks of 8 bits
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            if len(byte) == 8:
                utf8_string += chr(int(byte, 2))
        return utf8_string