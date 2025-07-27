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
        positions = []
        i = 0
        while i <= self.textLen - self.patLen:
            mismatch_pos = self.mismatch_in_text(i)
            if mismatch_pos == -1:
                positions.append(i)
                i += self.patLen
            else:
                char = self.text[mismatch_pos]
                match_pos = self.match_in_pattern(char)
                if match_pos == -1:
                    i += mismatch_pos + 1
                else:
                    i += mismatch_pos - match_pos
        return positions