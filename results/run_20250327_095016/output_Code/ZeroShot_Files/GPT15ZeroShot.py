class BoyerMooreSearch:
    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        """
        self.text = text
        self.pattern = pattern
        self.pattern_length = len(pattern)
        self.text_length = len(text)
        self.bad_char_table = self.create_bad_char_table()

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        """
        for i in range(self.pattern_length - 1, -1, -1):
            if self.pattern[i] == char:
                return i
        return -1

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        for i in range(self.pattern_length):
            if self.pattern[i] != self.text[currentPos + i]:
                return i
        return -1

    def create_bad_char_table(self):
        """
        Creates the bad character table used in the Boyer-Moore algorithm.
        :return: A dictionary with the rightmost occurrence of each character in the pattern.
        """
        bad_char_table = {}
        for i in range(self.pattern_length):
            bad_char_table[self.pattern[i]] = i
        return bad_char_table

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.
        :return: A list of all positions of the pattern in the text, list.
        """
        results = []
        shift = 0

        while shift <= self.text_length - self.pattern_length:
            mismatch_index = self.mismatch_in_text(shift)

            if mismatch_index == -1:  # No mismatch found
                results.append(shift)
                shift += self.pattern_length
            else:
                # Calculate the shift using the bad character heuristic
                bad_char_index = self.match_in_pattern(self.text[shift + mismatch_index])
                if bad_char_index == -1:
                    shift += mismatch_index + 1
                else:
                    shift += max(1, mismatch_index - bad_char_index)

        return results