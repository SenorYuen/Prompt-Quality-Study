class BinaryDataProcessor:
    def __init__(self, binary_string):
        """
        Initialize the class with a binary string and clean it by removing all non 0 or 1 characters.
        
        Args:
            binary_string (str): The binary string to be processed.
        """
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        """
        Clean the binary string by removing all non 0 or 1 characters.
        """
        self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))

    def calculate_binary_info(self):
        """
        Calculate the binary string information, including the percentage of 0 and 1, and the total length of the binary string.
        
        Returns:
            dict: A dictionary containing the percentage of 0 and 1, and the total length of the binary string.
        """
        zero_count = self.binary_string.count('0')
        one_count = self.binary_string.count('1')
        total_length = len(self.binary_string)
        
        zero_percentage = zero_count / total_length if total_length > 0 else 0
        one_percentage = one_count / total_length if total_length > 0 else 0
        
        return {'Zeroes': zero_percentage, 'Ones': one_percentage, 'Bit length': total_length}

    def convert_to_ascii(self):
        """
        Convert the binary string to ascii string.
        
        Returns:
            str: The ascii string converted from the binary string.
        """
        ascii_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            ascii_string += chr(int(byte, 2))
        return ascii_string

    def convert_to_utf8(self):
        """
        Convert the binary string to utf-8 string.
        
        Returns:
            str: The utf-8 string converted from the binary string.
        """
        utf8_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i+8]
            utf8_string += chr(int(byte, 2))
        return utf8_string