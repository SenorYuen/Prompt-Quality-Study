class Manacher:
    """
    This is a class that implements the Manacher's algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        # Initialize the length to 0
        length = 0
        # Expand around the center while the characters on both sides are equal
        while center - diff - length >= 0 and center + diff + length < len(string) and string[center - diff - length] == string[center + diff + length]:
            length += 1
        return length - 1

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        # Transform the input string to handle even-length palindromes by inserting separators
        transformed_string = '|'.join(f'#{char}' for char in self.input_string) + '#|'
        n = len(transformed_string)
        p = [0] * n  # Array to store the length of the palindrome at each center
        center = 0
        right = 0

        # Iterate over the transformed string
        for i in range(1, n - 1):
            mirror = 2 * center - i  # Mirror of i with respect to center
            if i < right:
                p[i] = min(right - i, p[mirror])

            # Attempt to expand palindrome centered at i
            p[i] += self.palindromic_length(i, p[i], transformed_string)

            # Update center and right boundary if the palindrome expands beyond the current right boundary
            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Find the maximum length palindrome
        max_len, max_center = max((n, i) for i, n in enumerate(p))
        start = (max_center - max_len) // 2  # Calculate the start index in the original string
        return self.input_string[start:start + max_len]