import re
import string

class LongestWord:
    """
    This is a class allows to add words to a list and find the longest word in a given sentence by comparing the words with the ones in the word list.
    """

    def __init__(self):
        """
        Initialize a list of word.
        """
        # Initialize an empty list to store words
        self.word_list = []

    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """
        # Append the input word to the word list
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        """
        # Remove punctuation marks from the sentence
        sentence = re.sub('['+string.punctuation+']', '', sentence)
        
        # Split the sentence into a list of words
        words = sentence.split()
        
        # Initialize the longest word and its length
        longest_word = ''
        max_length = 0
        
        # Iterate over each word in the sentence
        for word in words:
            # Check if the word is in the word list and its length is greater than the current max length
            if word in self.word_list and len(word) > max_length:
                # Update the longest word and its length
                longest_word = word
                max_length = len(word)
        
        # Return the longest word
        return longest_word