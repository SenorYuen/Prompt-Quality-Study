class BoyerMooreSearch:
    def __init__(self, text, pattern):
        # Initialize the text and pattern
        self.text = text
        self.pattern = pattern
        # Create a dictionary to store the last occurrence of each character in the pattern
        self.last_occurrence = {}
        for i in range(len(self.pattern)):
            self.last_occurrence[self.pattern[i]] = i

    def match_in_pattern(self, char):
        # Find the rightmost occurrence of a character in the pattern
        # Return -1 if the character is not found in the pattern
        return self.last_occurrence.get(char, -1)

    def mismatch_in_text(self, currentPos):
        # Compare the pattern with the text starting from the current position
        for i in range(len(self.pattern)):
            # If the characters do not match, return the position of the mismatch
            if currentPos + i >= len(self.text) or self.text[currentPos + i] != self.pattern[i]:
                return currentPos + i
        # If the entire pattern matches, return -1
        return -1

    def bad_character_heuristic(self):
        # Initialize a list to store the positions of the pattern in the text
        positions = []
        # Initialize the current position in the text
        currentPos = 0
        while currentPos <= len(self.text) - len(self.pattern):
            # Find the position of the first mismatch between the pattern and the text
            mismatchPos = self.mismatch_in_text(currentPos)
            # If the pattern matches the text at the current position, add the position to the list
            if mismatchPos == -1:
                positions.append(currentPos)
                # Move the current position to the right of the match
                currentPos += len(self.pattern)
            else:
                # Move the current position based on the bad character heuristic
                char = self.text[mismatchPos]
                shift = max(1, mismatchPos - self.match_in_pattern(char))
                currentPos += shift
        return positions