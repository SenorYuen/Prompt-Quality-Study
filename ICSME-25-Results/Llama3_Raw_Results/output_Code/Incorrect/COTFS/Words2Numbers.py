class Words2Numbers:
    def __init__(self, city=None):
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
        for word in textnum.replace('-', ' ').split():
            if word in self.numwords:
                scale, increment = self.numwords[word]
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
            elif word in self.ordinal_words:
                scale = self.ordinal_words[word]
                current = current * scale + scale
            elif word in ['hundred', 'thousand', 'million', 'billion', 'trillion']:
                current *= self.numwords[word][0]
            else:
                raise ValueError("Invalid word: " + word)
        return str(result + current)

    def is_valid_input(self, textnum):
        try:
            self.text2int(textnum)
            return True
        except ValueError:
            return False