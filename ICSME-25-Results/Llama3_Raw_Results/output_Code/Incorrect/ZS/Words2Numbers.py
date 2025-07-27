class Words2Numbers:

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
        :return: string, the final converted integer string
        """
        # Split the input string into words
        current = result = 0
        textnum = textnum.replace('-', ' ')
        words = textnum.split()
        
        # Iterate over each word in the input string
        for word in words:
            # Check if the word is in the numwords dictionary
            if word in self.numwords:
                scale, increment = self.numwords[word]
                # Update the current and result values
                current = current * scale + increment
                # If the scale is greater than 1, update the result
                if scale > 1:
                    result += current
                    current = 0
            # If the word is not in the numwords dictionary, check if it's an ordinal word
            elif word in self.ordinal_words:
                # Update the current value
                current = self.ordinal_words[word]
            # If the word is not in the numwords dictionary or ordinal words, check if it's a word with an ordinal ending
            else:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        # Update the current value
                        current = int(word[:-len(ending)].replace(replacement, ''))
                        break
                else:
                    # If the word is not recognized, raise a ValueError
                    raise ValueError("Invalid input: {}".format(word))
        
        # Add the current value to the result
        result += current
        return str(result)


    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :return: True if input is valid, False otherwise.
        """
        # Split the input string into words
        textnum = textnum.replace('-', ' ')
        words = textnum.split()
        
        # Iterate over each word in the input string
        for word in words:
            # Check if the word is in the numwords dictionary or ordinal words
            if word not in self.numwords and word not in self.ordinal_words:
                # Check if the word is a word with an ordinal ending
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        break
                else:
                    # If the word is not recognized, return False
                    return False
        # If all words are recognized, return True
        return True


# Example usage:
w2n = Words2Numbers()
print(w2n.text2int("one hundred and twenty five"))  # Output: 125
print(w2n.is_valid_input("one hundred and twenty five"))  # Output: True