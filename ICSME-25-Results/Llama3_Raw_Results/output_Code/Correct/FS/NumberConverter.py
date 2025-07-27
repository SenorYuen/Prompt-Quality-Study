class NumberConverter:
    """
    The class allows to convert decimal to binary, octal and hexadecimal respectively and contrarily
    """

    @staticmethod
    def decimal_to_binary(decimal_num):
        # Convert a number from decimal format to binary format using built-in bin() function
        # The bin() function returns a string that starts with '0b' to indicate it's a binary number, so we slice the string to remove the first two characters
        return bin(decimal_num)[2:]

    @staticmethod
    def binary_to_decimal(binary_num):
        # Convert a number from binary format to decimal format using built-in int() function with base 2
        return int(binary_num, 2)

    @staticmethod
    def decimal_to_octal(decimal_num):
        # Convert a number from decimal format to octal format using built-in oct() function
        # The oct() function returns a string that starts with '0o' to indicate it's an octal number, so we slice the string to remove the first two characters
        return oct(decimal_num)[2:]

    @staticmethod
    def octal_to_decimal(octal_num):
        # Convert a number from octal format to decimal format using built-in int() function with base 8
        return int(octal_num, 8)

    @staticmethod
    def decimal_to_hex(decimal_num):
        # Convert a number from decimal format to hex format using built-in hex() function
        # The hex() function returns a string that starts with '0x' to indicate it's a hex number, so we slice the string to remove the first two characters
        return hex(decimal_num)[2:]

    @staticmethod
    def hex_to_decimal(hex_num):
        # Convert a number from hex format to decimal format using built-in int() function with base 16
        return int(hex_num, 16)