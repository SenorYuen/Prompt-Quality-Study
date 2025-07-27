class BinaryDataProcessor:
    def __init__(self, binary_string):
        # Clean the binary string by removing all non 0 or 1 characters
        self.binary_string = self.clean_non_binary_chars(binary_string)

    def clean_non_binary_chars(self, binary_string):
        # Use a list comprehension to filter out non 0 or 1 characters
        return ''.join([char for char in binary_string if char in '01'])

    def calculate_binary_info(self):
        # Calculate the total length of the binary string
        total_length = len(self.binary_string)
        
        # Calculate the percentage of 0 and 1 in the binary string
        zero_percentage = (self.binary_string.count('0') / total_length) * 100 if total_length > 0 else 0
        one_percentage = (self.binary_string.count('1') / total_length) * 100 if total_length > 0 else 0
        
        # Return the binary string information as a dictionary
        return {
            'total_length': total_length,
            'zero_percentage': zero_percentage,
            'one_percentage': one_percentage
        }

    def convert_to_ascii(self):
        # Split the binary string into 8-bit chunks
        binary_chunks = [self.binary_string[i:i+8] for i in range(0, len(self.binary_string), 8)]
        
        # Convert each binary chunk to an ASCII character
        ascii_string = ''
        for chunk in binary_chunks:
            if len(chunk) < 8:
                break  # Ignore incomplete chunks
            ascii_char = chr(int(chunk, 2))
            ascii_string += ascii_char
        
        # Return the ASCII string
        return ascii_string

    def convert_to_utf8(self):
        # Split the binary string into 8-bit chunks
        binary_chunks = [self.binary_string[i:i+8] for i in range(0, len(self.binary_string), 8)]
        
        # Convert each binary chunk to a UTF-8 character
        utf8_string = ''
        for chunk in binary_chunks:
            if len(chunk) < 8:
                break  # Ignore incomplete chunks
            utf8_char = chr(int(chunk, 2))
            utf8_string += utf8_char
        
        # Return the UTF-8 string
        return utf8_string

# Example usage:
binary_data = BinaryDataProcessor('10101010')
print(binary_data.calculate_binary_info())
print(binary_data.convert_to_ascii())
print(binary_data.convert_to_utf8())