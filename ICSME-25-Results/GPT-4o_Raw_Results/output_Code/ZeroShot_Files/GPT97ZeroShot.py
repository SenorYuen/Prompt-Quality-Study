def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :return: string, the final converted integer string
        """
        current = result = 0
        # Split the input text into words
        words = textnum.lower().replace('-', ' ').split()

        for word in words:
            # Handle ordinal words separately
            if word in self.ordinal_words:
                current += self.ordinal_words[word]
            else:
                # Handle endings for ordinal words
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = word[:len(word) - len(ending)] + replacement
                        if word in self.numwords:
                            scale, increment = self.numwords[word]
                            current = current * scale + increment
                            break

            if word in self.numwords:
                scale, increment = self.numwords[word]
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0

        return str(result + current)

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :return: True if input is valid, False otherwise.
        """
        words = textnum.lower().replace('-', ' ').split()

        for word in words:
            # Check if the word is a valid unit, ten, scale, or ordinal
            if word not in self.numwords and word not in self.ordinal_words:
                # Check if the word can be converted by removing ordinal endings
                valid = False
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = word[:len(word) - len(ending)] + replacement
                        if word in self.numwords:
                            valid = True
                            break
                if not valid:
                    return False

        return True