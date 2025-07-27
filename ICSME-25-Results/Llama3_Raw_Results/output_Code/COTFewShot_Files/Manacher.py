class Manacher:
    def __init__(self, input_string):
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        # Preprocess the string to handle even-length palindromes
        processed_string = '#' + '#'.join(string) + '#'
        
        # Initialize the length of the palindrome
        length = 0
        
        # Check if the characters at the current positions are equal
        while center - diff >= 0 and center + diff < len(processed_string) and processed_string[center - diff] == processed_string[center + diff]:
            # If they are equal, increment the difference
            diff += 1
        
        # The length of the palindrome is twice the difference minus 1 (for the center character)
        length = 2 * (diff - 1)
        
        return length

    def palindromic_string(self):
        # Preprocess the string to handle even-length palindromes
        processed_string = '#' + '#'.join(self.input_string) + '#'
        
        # Initialize the maximum length and center of the palindrome
        max_length = 0
        center = 0
        
        # Iterate over the processed string
        for i in range(len(processed_string)):
            # Calculate the length of the palindrome centered at the current position
            length = self.palindromic_length(i, 1, processed_string)
            
            # If the length of the current palindrome is greater than the maximum length, update the maximum length and center
            if length > max_length:
                max_length = length
                center = i
        
        # Extract the longest palindromic substring from the processed string
        palindromic_substring = processed_string[center - max_length // 2: center + max_length // 2 + 1]
        
        # Remove the '#' characters from the palindromic substring
        palindromic_substring = palindromic_substring.replace('#', '')
        
        return palindromic_substring