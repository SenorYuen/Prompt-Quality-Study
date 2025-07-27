# The class allows to convert decimal to binary, octal and hexadecimal respectively and contrarily
class NumberConverter:
    @staticmethod
    def decimal_to_binary(decimal_num):
        # Convert a number from decimal format to binary format.
        # :return: str, the binary representation of an integer.
        return bin(decimal_num)[2:]  # Remove '0b' prefix from binary string

    @staticmethod
    def binary_to_decimal(binary_num):
        # Convert a number from binary format to decimal format.
        # :return: int, the decimal representation of binary number str.
        return int(binary_num, 2)  # Base 2 for binary conversion

    @staticmethod
    def decimal_to_octal(decimal_num):
        # Convert a number from decimal format to octal format.
        # :return: str, the octal representation of an integer.
        return oct(decimal_num)[2:]  # Remove '0o' prefix from octal string

    @staticmethod
    def octal_to_decimal(octal_num):
        # Convert a number from octal format to decimal format.
        # :return: int, the decimal representation of octal number str.
        return int(octal_num, 8)  # Base 8 for octal conversion

    @staticmethod
    def decimal_to_hex(decimal_num):
        # Convert a number from decimal format to hex format.
        # :return hex_num: str, the hex representation of an integer.
        return hex(decimal_num)[2:]  # Remove '0x' prefix from hex string

    @staticmethod
    def hex_to_decimal(hex_num):
        # Convert a number from hex format to decimal format.
        # :return: int, the decimal representation of hex number str.
        return int(hex_num, 16)  # Base 16 for hex conversion


# Example usage:
if __name__ == "__main__":
    decimal_num = 123
    binary_num = NumberConverter.decimal_to_binary(decimal_num)
    print(f"Decimal {decimal_num} to Binary: {binary_num}")

    octal_num = NumberConverter.decimal_to_octal(decimal_num)
    print(f"Decimal {decimal_num} to Octal: {octal_num}")

    hex_num = NumberConverter.decimal_to_hex(decimal_num)
    print(f"Decimal {decimal_num} to Hex: {hex_num}")

    decimal_from_binary = NumberConverter.binary_to_decimal(binary_num)
    print(f"Binary {binary_num} to Decimal: {decimal_from_binary}")

    decimal_from_octal = NumberConverter.octal_to_decimal(octal_num)
    print(f"Octal {octal_num} to Decimal: {decimal_from_octal}")

    decimal_from_hex = NumberConverter.hex_to_decimal(hex_num)
    print(f"Hex {hex_num} to Decimal: {decimal_from_hex}")