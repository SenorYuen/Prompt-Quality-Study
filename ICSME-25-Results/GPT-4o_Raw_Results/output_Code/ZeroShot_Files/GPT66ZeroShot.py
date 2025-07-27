import re

class NumericEntityUnescaper:
    def __init__(self):
        pass

    def replace(self, string):
        """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        """
        # Regex to match numeric character references, both decimal (&#123;) and hexadecimal (&#x1A;)
        entity_pattern = re.compile(r'&#(x?[0-9A-Fa-f]+);')

        # Function to convert matched numeric reference to character
        def replace_entity(match):
            entity = match.group(1)
            if entity.startswith('x') or entity.startswith('X'):
                # Hexadecimal entity
                code_point = int(entity[1:], 16)
            else:
                # Decimal entity
                code_point = int(entity)
            try:
                # Convert code point to character
                return chr(code_point)
            except ValueError:
                # If conversion fails, return the original match
                return match.group(0)

        # Substitute all numeric references using the replace_entity function
        return entity_pattern.sub(replace_entity, string)

    @staticmethod
    def is_hex_char(char):
        """
        Determines whether a given character is a hexadecimal digit.
        :param char: str, a single character to check.
        :return: bool, True if the character is a hexadecimal digit, False otherwise.
        """
        # Check if the character is a valid hexadecimal digit (0-9, a-f, A-F)
        return char.isdigit() or ('a' <= char.lower() <= 'f')