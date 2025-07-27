# This is a class that implements a Manacher algorithm to find the Longest palindromic substring in a given string.

class Manacher:
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        """
        # Preprocess the input string to handle even-length palindromes
        self.input_string = '#' + '#'.join(input_string) + '#'
        self.length = len(self.input_string)

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :return: The length of the palindromic substring, int.
        """
        # Base case: if the difference is 0, return 0
        if diff == 0:
            return 0
        
        # Check if the characters at the current positions are equal
        while center - diff >= 0 and center + diff < self.length and string[center - diff] == string[center + diff]:
            # If they are equal, increase the difference
            diff += 1
        
        # Return the length of the palindromic substring
        return diff - 1

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        # Initialize variables to store the maximum length and center of the longest palindromic substring
        max_length = 0
        center = 0
        
        # Iterate over the string to find the longest palindromic substring
        for i in range(self.length):
            # Calculate the length of the palindromic substring centered at the current position
            length = self.palindromic_length(i, 1, self.input_string)
            
            # Update the maximum length and center if a longer palindromic substring is found
            if length > max_length:
                max_length = length
                center = i
        
        # Extract the longest palindromic substring from the input string
        longest_palindromic_substring = self.input_string[center - max_length:center + max_length + 1]
        
        # Remove the '#' characters from the longest palindromic substring
        longest_palindromic_substring = longest_palindromic_substring.replace('#', '')
        
        # Return the longest palindromic substring
        return longest_palindromic_substring

# Example usage:
manacher = Manacher("babad")
print(manacher.palindromic_string())  # Output: "bab"