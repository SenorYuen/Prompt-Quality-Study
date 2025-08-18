'''
# The class allows to convert  decimal to binary, octal and hexadecimal repectively and contrarily

class NumberConverter:
    @staticmethod
    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :return: str, the binary representation of an integer.
        """

    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :return: int, the decimal representation of binary number str.
        """


    @staticmethod
    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :return: str, the octal representation of an integer.
        """

    @staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :return: int, the decimal representation of octal number str.
        """

    @staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :return hex_num: str, the hex representation of an integer.
        """

    @staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :return: int, the decimal representation of hex number str.
        """

'''


class NumberConverter:
    @staticmethod
    def decimal_to_binary(decimal_num):
        binary_num = bin(decimal_num)[2:]
        return binary_num

    @staticmethod
    def binary_to_decimal(binary_num):
        decimal_num = int(binary_num, 2)
        return decimal_num

    @staticmethod
    def decimal_to_octal(decimal_num):
        octal_num = oct(decimal_num)[2:]
        return octal_num

    @staticmethod
    def octal_to_decimal(octal_num):
        decimal_num = int(octal_num, 8)
        return decimal_num

    @staticmethod
    def decimal_to_hex(decimal_num):
        hex_num = hex(decimal_num)[2:]
        return hex_num

    @staticmethod
    def hex_to_decimal(hex_num):
        decimal_num = int(hex_num, 16)
        return decimal_num
