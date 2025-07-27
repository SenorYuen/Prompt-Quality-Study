import re
import string

class LongestWord:
    """
    This is a class that allows adding words to a list and finding the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of words.
        """
        self.word_list = []

    def add_word(self, word):
        """
        Append the input word into self.word_list
        :param word: str, input word
        """
        # Add the word to the word_list
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of words. Find the longest split word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest split word that is in the self.word_list. return '' if self.word_list is empty.
        """
        # Remove punctuation from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Split the sentence into words
        words = sentence.split()
        
        # Initialize the longest word variable
        longest_word = ''
        
        # Iterate over each word in the sentence
        for word in words:
            # Check if the word is in the word_list and is longer than the current longest_word
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
        
        # Return the longest word found
        return longest_word

# Example usage:
# longestWord = LongestWord()
# longestWord.add_word('A')
# longestWord.add_word('aM')
# print(longestWord.find_longest_word('I am a student.'))  # Output: 'a'