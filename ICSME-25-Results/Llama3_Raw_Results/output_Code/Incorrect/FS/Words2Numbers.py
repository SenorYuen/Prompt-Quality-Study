class Words2Numbers:
    """
    The class provides a text-to-number conversion utility, allowing conversion of written numbers (in words) to their numerical representation.
    """

    def __init__(self):
        """
        Initialize the word lists and dictionaries required for conversion
        """
        self.numwords = {}
        self.units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.scales = ["hundred", "thousand", "million", "billion", "trillion"]

        self.numwords["and"] = (1, 0)
        for idx, word in enumerate(self.units):
            self.numwords[word] = (1, idx)
        for idx, word in enumerate(self.tens):
            self.numwords[word] = (1, idx * 10)
        for idx, word in enumerate(self.scales):
            self.numwords[word] = (10 ** (idx * 3 or 2), 0)

        self.ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        self.ordinal_endings = [('ieth', 'y'), ('th', '')]


    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
        # Replace hyphens with spaces to handle compound numbers
        textnum = textnum.replace('-', ' ')
        
        # Split the input string into words
        current = result = 0
        for word in textnum.split():
            # Check if the word is in the numwords dictionary
            if word in self.numwords:
                # Get the value and scale of the word
                scale, value = self.numwords[word]
                # If the scale is 1, add the value to the current number
                if scale == 1:
                    current += value
                # If the scale is greater than 1, multiply the current number by the scale
                else:
                    current *= scale
            # If the word is not in the numwords dictionary, it may be an ordinal word
            elif word in self.ordinal_words:
                # Get the value of the ordinal word
                value = self.ordinal_words[word]
                # Add the value to the current number
                current += value
            # If the word is not in the numwords or ordinal_words dictionaries, it may be a hyphenated number
            else:
                # Try to split the word into two parts
                for ending in self.ordinal_endings:
                    if word.endswith(ending[0]):
                        # Get the base word and the ending
                        base_word = word[:-len(ending[0])] + ending[1]
                        # Check if the base word is in the numwords dictionary
                        if base_word in self.numwords:
                            # Get the value and scale of the base word
                            scale, value = self.numwords[base_word]
                            # Add the value to the current number
                            current += value
                            break
                else:
                    # If the word is not recognized, raise a ValueError
                    raise ValueError("Invalid input: " + word)
            # If the current number is greater than 0, add it to the result and reset the current number
            if current > 0:
                result += current
                current = 0
        # Return the result as a string
        return str(result)


    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        # Replace hyphens with spaces to handle compound numbers
        textnum = textnum.replace('-', ' ')
        
        # Split the input string into words
        for word in textnum.split():
            # Check if the word is in the numwords dictionary
            if word in self.numwords:
                continue
            # If the word is not in the numwords dictionary, it may be an ordinal word
            elif word in self.ordinal_words:
                continue
            # If the word is not in the numwords or ordinal_words dictionaries, it may be a hyphenated number
            else:
                # Try to split the word into two parts
                for ending in self.ordinal_endings:
                    if word.endswith(ending[0]):
                        # Get the base word and the ending
                        base_word = word[:-len(ending[0])] + ending[1]
                        # Check if the base word is in the numwords dictionary
                        if base_word in self.numwords:
                            break
                else:
                    # If the word is not recognized, return False
                    return False
        # If all words are recognized, return True
        return True