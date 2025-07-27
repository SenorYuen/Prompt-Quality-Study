class BoyerMooreSearch:
    """
    This is a class that implements the Boyer-Moore algorithm for string searching, 
    which is used to find occurrences of a pattern within a given text.
    """

    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        """
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        """
        # Iterate over the pattern from right to left to find the rightmost occurrence of the character
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] == char:
                return i
        # Return -1 if the character is not found in the pattern
        return -1

    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        # Iterate over the pattern and the corresponding substring in the text
        for i in range(self.patLen):
            # Check if the current position is within the text boundaries
            if currentPos + i >= self.textLen:
                return -1
            # Check if the characters at the current positions in the pattern and the text match
            if self.pattern[i] != self.text[currentPos + i]:
                # Return the position of the first mismatch
                return currentPos + i
        # Return -1 if no mismatch is found
        return -1

    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text using the bad character heuristic.
        :return: A list of all positions of the pattern in the text, list.
        """
        # Initialize an empty list to store the positions of the pattern in the text
        positions = []
        # Initialize the current position in the text
        currentPos = 0
        # Iterate over the text
        while currentPos <= self.textLen - self.patLen:
            # Find the position of the first mismatch between the pattern and the text
            mismatchPos = self.mismatch_in_text(currentPos)
            # Check if a mismatch is found
            if mismatchPos == -1:
                # If no mismatch is found, the pattern is found at the current position
                positions.append(currentPos)
                # Move the current position to the next possible position
                currentPos += self.patLen
            else:
                # If a mismatch is found, move the current position based on the bad character heuristic
                char = self.text[mismatchPos]
                matchPos = self.match_in_pattern(char)
                if matchPos == -1:
                    # If the character is not found in the pattern, move the current position to the next character
                    currentPos += 1
                else:
                    # If the character is found in the pattern, move the current position based on the match position
                    currentPos += mismatchPos - matchPos
        # Return the list of positions of the pattern in the text
        return positions