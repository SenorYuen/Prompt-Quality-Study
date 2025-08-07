import re
import string

class LongestWord:
    def __init__(self):
        """
        Initialize a list of words.
        """
        self.word_list = []  # Initialize an empty list to store words

    def add_word(self, word):
        """
        Append the input word into self.word_list
        """
        self.word_list.append(word)  # Add the word to the word list

    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of words. 
        Find the longest split word that is in the self.word_list.
        Words are strictly case sensitive.
        :return str: longest split word that is in the self.word_list. return '' if self.word_list is empty.
        """
        # Remove punctuation from the sentence and split it into words
        words_in_sentence = re.findall(r'\b\w+\b', sentence)

        # Initialize variables to track the longest word
        longest_word = ''
        max_length = 0

        # Iterate over each word in the sentence
        for word in words_in_sentence:
            # Check if the word is in the word list and is longer than the current longest word
            if word in self.word_list and len(word) > max_length:
                longest_word = word
                max_length = len(word)

        return longest_word  # Return the longest word found