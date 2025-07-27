class BinaryDataProcessor:
    def __init__(self, binary_string):
        self.binary_string = binary_string
        self.clean_non_binary_chars()

    def clean_non_binary_chars(self):
        self.binary_string = ''.join(filter(lambda x: x in '01', self.binary_string))

    def calculate_binary_info(self):
        length = len(self.binary_string)
        count_zeros = self.binary_string.count('0')
        count_ones = self.binary_string.count('1')
        return {
            'Zeroes': count_zeros / length if length > 0 else 0,
            'Ones': count_ones / length if length > 0 else 0,
            'Bit length': length
        }

    def convert_to_ascii(self):
        n = 8
        ascii_string = ''.join(chr(int(self.binary_string[i:i + n], 2)) for i in range(0, len(self.binary_string), n))
        return ascii_string

    def convert_to_utf8(self):
        n = 8
        utf8_bytes = bytes(int(self.binary_string[i:i + n], 2) for i in range(0, len(self.binary_string), n))
        return utf8_bytes.decode('utf-8', errors='ignore')