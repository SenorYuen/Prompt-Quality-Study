class NumericEntityUnescaper:
    def __init__(self):
        # Initialize the class, no actions required
        pass

    def replace(self, string):
        # Initialize an empty string to store the result
        result = ""
        # Initialize a flag to track if we are currently processing a numeric entity
        in_entity = False
        # Initialize a string to store the current entity
        current_entity = ""
        
        # Iterate over each character in the input string
        for char in string:
            # If we are not currently processing an entity and encounter an ampersand
            if not in_entity and char == "&":
                # Set the flag to True and append the ampersand to the current entity
                in_entity = True
                current_entity += char
            # If we are currently processing an entity and encounter a semicolon
            elif in_entity and char == ";":
                # Set the flag to False and append the semicolon to the current entity
                in_entity = False
                current_entity += char
                # If the entity starts with '&#' and the rest of the entity is a decimal number
                if current_entity.startswith("&#") and current_entity[2:-1].isdigit():
                    # Replace the entity with the corresponding Unicode character
                    result += chr(int(current_entity[2:-1]))
                # If the entity starts with '&#x' and the rest of the entity is a hexadecimal number
                elif current_entity.startswith("&#x") and all(self.is_hex_char(c) for c in current_entity[3:-1]):
                    # Replace the entity with the corresponding Unicode character
                    result += chr(int(current_entity[3:-1], 16))
                # Reset the current entity
                current_entity = ""
            # If we are currently processing an entity
            elif in_entity:
                # Append the character to the current entity
                current_entity += char
            # If we are not currently processing an entity
            else:
                # Append the character to the result
                result += char
        
        # Return the result
        return result

    @staticmethod
    def is_hex_char(char):
        # Check if the character is a hexadecimal digit
        return char.isdigit() or char.lower() in "abcdef"