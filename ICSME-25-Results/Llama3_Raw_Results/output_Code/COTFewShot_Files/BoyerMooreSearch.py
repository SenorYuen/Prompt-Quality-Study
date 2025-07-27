class BoyerMooreSearch:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.textLen = len(text)
        self.patLen = len(pattern)

    def match_in_pattern(self, char):
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        for i in range(self.patLen):
            if currentPos + i >= self.textLen or self.text[currentPos + i] != self.pattern[i]:
                return currentPos + i
        return -1

    def bad_character_heuristic(self):
        occurrences = []
        i = 0
        while i <= self.textLen - self.patLen:
            mismatchPos = self.mismatch_in_text(i)
            if mismatchPos == -1:
                occurrences.append(i)
                i += self.patLen
            else:
                char = self.text[mismatchPos]
                shift = self.patLen - self.match_in_pattern(char) - 1
                if shift < 1:
                    shift = 1
                i += shift
        return occurrences