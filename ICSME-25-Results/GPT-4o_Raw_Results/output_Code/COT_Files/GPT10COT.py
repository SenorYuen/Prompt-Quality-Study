class BinaryDataProcessor:
    def __init__(self, binary_string):
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))

    def calculate_binary_info(self):
        zero_count = self.binary_string.count('0')
        one_count = self.binary_string.count('1')
        total_length = len(self.binary_string)
        return {
            'Zeroes': zero_count / total_length,
            'Ones': one_count / total_length,
            'Bit length': total_length
        }

    def convert_to_ascii(self):
        ascii_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i + 8]
            ascii_string += chr(int(byte, 2))
        return ascii_string

    def convert_to_utf8(self):
        utf8_string = ''
        for i in range(0, len(self.binary_string), 8):
            byte = self.binary_string[i:i + 8]
            utf8_string += chr(int(byte, 2))
        return utf8_string