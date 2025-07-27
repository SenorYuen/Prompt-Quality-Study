class Manacher:
    def __init__(self, input_string):
        # Initialize the Manacher class with the given input_string.
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        # Recursively calculate the length of the palindromic substring based on a given center, difference value, and input string.
        if center - diff < 0 or center + diff >= len(string) or string[center - diff] != string[center + diff]:
            return diff * 2 + 1 if string[center] != '|' else diff * 2
        else:
            return self.palindromic_length(center, diff + 1, string)

    def palindromic_string(self):
        # Preprocess the input string to handle even-length palindromes.
        string = '|'.join(self.input_string)
        string = '|' + string + '|'
        
        # Initialize variables to store the maximum length and center of the longest palindromic substring.
        max_length = 0
        center = 0
        
        # Iterate over the preprocessed string to find the longest palindromic substring.
        for i in range(len(string)):
            length = self.palindromic_length(i, 0, string)
            if length > max_length:
                max_length = length
                center = i
        
        # Extract the longest palindromic substring from the preprocessed string.
        longest_palindrome = string[center - max_length // 2 + 1:center + max_length // 2]
        
        # Remove the '|' characters from the longest palindromic substring.
        longest_palindrome = longest_palindrome.replace('|', '')
        
        return longest_palindrome