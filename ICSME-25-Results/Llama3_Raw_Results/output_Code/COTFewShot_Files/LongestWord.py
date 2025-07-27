import re
import string

class LongestWord:
    def __init__(self):
        self.word_list = []

    def add_word(self, word):
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        # Remove punctuation marks and split the sentence into a list of words
        words = re.sub('['+string.punctuation+']', '', sentence).split()
        
        # Initialize the longest word and its length
        longest_word = ''
        max_length = 0
        
        # Iterate over each word in the sentence
        for word in words:
            # Check if the word is in the word list and its length is greater than the current max length
            if word in self.word_list and len(word) > max_length:
                longest_word = word
                max_length = len(word)
        
        return longest_word