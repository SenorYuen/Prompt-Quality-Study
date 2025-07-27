class NumericEntityUnescaper:
    def __init__(self):
        pass

    def replace(self, string):
        # Initialize an empty string to store the result
        result = ""
        
        # Initialize an empty string to store the numeric entity
        entity = ""
        
        # Initialize a flag to indicate whether we are currently processing a numeric entity
        in_entity = False
        
        # Iterate over each character in the input string
        i = 0
        while i < len(string):
            # If the character is an ampersand and we are not currently processing a numeric entity,
            # it could be the start of a numeric entity
            if string[i] == '&' and not in_entity:
                # Check if the next characters are '#x' or '#'
                if i + 2 < len(string) and string[i+1:i+3] == '#x':
                    in_entity = True
                    entity = ''
                    i += 3
                elif i + 1 < len(string) and string[i+1] == '#':
                    in_entity = True
                    entity = ''
                    i += 2
                else:
                    result += string[i]
                    i += 1
            # If we are currently processing a numeric entity and the character is a semicolon,
            # it could be the end of the numeric entity
            elif string[i] == ';' and in_entity:
                # Try to convert the numeric entity to a Unicode character
                try:
                    if entity.startswith('x'):
                        result += chr(int(entity[1:], 16))
                    else:
                        result += chr(int(entity))
                except ValueError:
                    # If the conversion fails, just append the entity to the result as is
                    result += '&' + entity + ';'
                in_entity = False
                entity = ''
                i += 1
            # If we are currently processing a numeric entity and the character is a digit or a letter,
            # add it to the entity
            elif in_entity:
                entity += string[i]
                i += 1
            # If we are not currently processing a numeric entity, just append the character to the result
            else:
                result += string[i]
                i += 1
        return result

    @staticmethod
    def is_hex_char(char):
        # Check if the character is a digit or a letter between 'a' and 'f' (inclusive) or between 'A' and 'F' (inclusive)
        return char.isdigit() or ('a' <= char <= 'f') or ('A' <= char <= 'F')