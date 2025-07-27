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
            if self.pattern[i] != self.text[currentPos + i]:
                return i
        return -1

    def bad_character_heuristic(self):
        positions = []
        currentPos = 0
        while currentPos <= self.textLen - self.patLen:
            mismatchIndex = self.mismatch_in_text(currentPos)
            if mismatchIndex == -1:
                positions.append(currentPos)
                currentPos += self.patLen
            else:
                charIndex = self.match_in_pattern(self.text[currentPos + mismatchIndex])
                shift = max(1, mismatchIndex - charIndex)
                currentPos += shift
        return positions