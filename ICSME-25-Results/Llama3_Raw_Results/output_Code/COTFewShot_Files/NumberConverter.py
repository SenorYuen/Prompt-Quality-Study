class NumberConverter:
    @staticmethod
    def decimal_to_binary(decimal_num):
        # Convert a number from decimal format to binary format
        return bin(decimal_num)[2:]

    @staticmethod
    def binary_to_decimal(binary_num):
        # Convert a number from binary format to decimal format
        return int(binary_num, 2)

    @staticmethod
    def decimal_to_octal(decimal_num):
        # Convert a number from decimal format to octal format
        return oct(decimal_num)[2:]

    @staticmethod
    def octal_to_decimal(octal_num):
        # Convert a number from octal format to decimal format
        return int(octal_num, 8)

    @staticmethod
    def decimal_to_hex(decimal_num):
        # Convert a number from decimal format to hex format
        return hex(decimal_num)[2:]

    @staticmethod
    def hex_to_decimal(hex_num):
        # Convert a number from hex format to decimal format
        return int(hex_num, 16)