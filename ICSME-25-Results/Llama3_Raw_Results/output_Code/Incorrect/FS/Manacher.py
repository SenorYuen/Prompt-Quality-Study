class Manacher:
    """
    This is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    # Function to preprocess the input string by inserting a special character between each character
    def preprocess(self, string):
        # Initialize an empty string to store the preprocessed string
        preprocessed_string = ""
        # Iterate over each character in the input string
        for char in string:
            # Append the special character and the current character to the preprocessed string
            preprocessed_string += "|" + char
        # Append the special character at the end of the preprocessed string
        preprocessed_string += "|"
        return preprocessed_string

    # Function to calculate the length of the palindromic substring based on a given center and input string
    def palindromic_length(self, center, string):
        # Initialize the length of the palindromic substring to 0
        length = 0
        # Initialize the left and right pointers
        left = center
        right = center
        # Iterate until the left or right pointer is out of bounds
        while left > 0 and right < len(string) - 1:
            # If the characters at the left and right pointers are equal, increment the length and move the pointers
            if string[left - 1] == string[right + 1]:
                length += 2
                left -= 1
                right += 1
            # If the characters at the left and right pointers are not equal, break the loop
            else:
                break
        return length

    # Function to find the longest palindromic substring in the given string
    def palindromic_string(self):
        # Preprocess the input string
        string = self.preprocess(self.input_string)
        # Initialize the maximum length and center of the longest palindromic substring
        max_length = 0
        center = 0
        # Iterate over each character in the preprocessed string
        for i in range(len(string)):
            # Calculate the length of the palindromic substring based on the current center
            length = self.palindromic_length(i, string)
            # If the length of the current palindromic substring is greater than the maximum length, update the maximum length and center
            if length > max_length:
                max_length = length
                center = i
        # Extract the longest palindromic substring from the preprocessed string
        palindromic_substring = string[center - max_length // 2: center + max_length // 2 + 1]
        # Remove the special characters from the longest palindromic substring
        palindromic_substring = palindromic_substring.replace("|", "")
        return palindromic_substring