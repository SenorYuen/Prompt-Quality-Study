class NumberConverter:
    @staticmethod
    def decimal_to_binary(decimal_num):
        """
        Convert a number from decimal format to binary format.
        :return: str, the binary representation of an integer.
        """
        # Use the built-in bin() function and remove '0b' prefix
        return bin(decimal_num)[2:]

    @staticmethod
    def binary_to_decimal(binary_num):
        """
        Convert a number from binary format to decimal format.
        :return: int, the decimal representation of binary number str.
        """
        # Use the int function with base 2 to convert binary to decimal
        return int(binary_num, 2)

    @staticmethod
    def decimal_to_octal(decimal_num):
        """
        Convert a number from decimal format to octal format.
        :return: str, the octal representation of an integer.
        """
        # Use the built-in oct() function and remove '0o' prefix
        return oct(decimal_num)[2:]

    @staticmethod
    def octal_to_decimal(octal_num):
        """
        Convert a number from octal format to decimal format.
        :return: int, the decimal representation of octal number str.
        """
        # Use the int function with base 8 to convert octal to decimal
        return int(octal_num, 8)

    @staticmethod
    def decimal_to_hex(decimal_num):
        """
        Convert a number from decimal format to hex format.
        :return hex_num: str, the hex representation of an integer.
        """
        # Use the built-in hex() function and remove '0x' prefix
        return hex(decimal_num)[2:]

    @staticmethod
    def hex_to_decimal(hex_num):
        """
        Convert a number from hex format to decimal format.
        :return: int, the decimal representation of hex number str.
        """
        # Use the int function with base 16 to convert hex to decimal
        return int(hex_num, 16)