class Manacher:
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        Preprocesses the string to handle even length palindromes by inserting '#' between characters.
        """
        self.input_string = input_string
        # Transform the input string by inserting '#' between each character and at the start and end
        self.transformed_string = '#' + '#'.join(input_string) + '#'
        # Array to store the length of the palindromic radius around each center
        self.palindrome_lengths = [0] * len(self.transformed_string)

    def palindromic_length(self, center, diff, string):
        """
        Calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :return: The length of the palindromic substring, int.
        """
        # Expand around the center as long as the characters match and within bounds
        while center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]:
            diff += 1
        # Return the length of the palindrome radius
        return diff - 1

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        center = 0
        right = 0
        max_length = 0
        max_center = 0

        for i in range(len(self.transformed_string)):
            # Mirror of the current position i around the center
            mirror = 2 * center - i

            if i < right:
                # Use previously calculated palindrome length if within bounds
                self.palindrome_lengths[i] = min(right - i, self.palindrome_lengths[mirror])

            # Try to expand the palindrome around the current center i
            self.palindrome_lengths[i] = self.palindromic_length(i, self.palindrome_lengths[i] + 1, self.transformed_string)

            # Update the center and right boundary if the palindrome expands beyond the current right boundary
            if i + self.palindrome_lengths[i] > right:
                center = i
                right = i + self.palindrome_lengths[i]

            # Update the maximum palindrome length and its center
            if self.palindrome_lengths[i] > max_length:
                max_length = self.palindrome_lengths[i]
                max_center = i

        # Calculate the start index of the longest palindrome in the original string
        start = (max_center - max_length) // 2
        # Return the longest palindromic substring
        return self.input_string[start:start + max_length]