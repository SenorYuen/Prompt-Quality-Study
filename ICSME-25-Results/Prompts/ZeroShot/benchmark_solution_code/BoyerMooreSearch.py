'''
#This is a class that implements the Boyer-Moore algorithm for string searching, which is used to find occurrences of a pattern within a given text.

class BoyerMooreSearch:
    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        """

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        """

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        """

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
'''

class BoyerMooreSearch:
    def __init__(self, text, pattern):
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)

    def match_in_pattern(self, char):
        for i in range(self.patLen - 1, -1, -1):
            if char == self.pattern[i]:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1

    def bad_character_heuristic(self):
        positions = []
        for i in range(self.textLen - self.patLen + 1):
            mismatch_index = self.mismatch_in_text(i)
            if mismatch_index == -1:
                positions.append(i)
            else:
                match_index = self.match_in_pattern(self.text[mismatch_index])
                i = (mismatch_index - match_index)
        return positions