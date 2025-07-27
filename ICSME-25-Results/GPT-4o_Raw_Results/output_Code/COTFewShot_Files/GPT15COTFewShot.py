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
            if self.text[currentPos + i] != self.pattern[i]:
                return i
        return -1

    def bad_character_heuristic(self):
        occurrences = []
        shift = 0
        while shift <= self.textLen - self.patLen:
            mismatchPos = self.mismatch_in_text(shift)
            if mismatchPos == -1:
                occurrences.append(shift)
                shift += 1
            else:
                charShift = mismatchPos - self.match_in_pattern(self.text[shift + mismatchPos])
                shift += max(1, charShift)
        return occurrences