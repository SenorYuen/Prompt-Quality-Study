class Words2Numbers:
    def __init__(self):
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
        current = result = 0
        words = textnum.replace('-', ' ').split()

        for word in words:
            if word in self.ordinal_words:
                scale, increment = (1, self.ordinal_words[word])
            else:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = word[:-len(ending)] + replacement

                if word not in self.numwords:
                    raise ValueError(f"Invalid word: {word}")

                scale, increment = self.numwords[word]

            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0

        return str(result + current)

    def is_valid_input(self, textnum):
        words = textnum.replace('-', ' ').split()
        for word in words:
            if word not in self.numwords and word not in self.ordinal_words:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = word[:-len(ending)] + replacement
                if word not in self.numwords:
                    return False
        return True