class NumberConverter:
    @staticmethod
    def decimal_to_binary(decimal_num: int) -> str:
        # Convert a decimal number to binary using built-in bin function
        # The bin function returns a string that starts with '0b' to indicate it's a binary number
        # We use string slicing to remove the '0b' prefix
        return bin(decimal_num)[2:]

    @staticmethod
    def binary_to_decimal(binary_num: str) -> int:
        # Convert a binary number to decimal using built-in int function with base 2
        return int(binary_num, 2)

    @staticmethod
    def decimal_to_octal(decimal_num: int) -> str:
        # Convert a decimal number to octal using built-in oct function
        # The oct function returns a string that starts with '0o' to indicate it's an octal number
        # We use string slicing to remove the '0o' prefix
        return oct(decimal_num)[2:]

    @staticmethod
    def octal_to_decimal(octal_num: str) -> int:
        # Convert an octal number to decimal using built-in int function with base 8
        return int(octal_num, 8)

    @staticmethod
    def decimal_to_hex(decimal_num: int) -> str:
        # Convert a decimal number to hex using built-in hex function
        # The hex function returns a string that starts with '0x' to indicate it's a hex number
        # We use string slicing to remove the '0x' prefix
        return hex(decimal_num)[2:]

    @staticmethod
    def hex_to_decimal(hex_num: str) -> int:
        # Convert a hex number to decimal using built-in int function with base 16
        return int(hex_num, 16)