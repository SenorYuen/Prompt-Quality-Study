import re
import string

class LongestWord:
    def __init__(self):
        # Initialize an empty list to store words
        self.word_list = []

    def add_word(self, word):
        # Append the input word into self.word_list
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        # Remove punctuation marks from the sentence
        sentence_without_punctuation = re.sub('['+string.punctuation+']', '', sentence)
        
        # Split the sentence into a list of words
        words_in_sentence = sentence_without_punctuation.split()
        
        # Initialize the longest word and its length
        longest_word = ''
        max_length = 0
        
        # Iterate over each word in the sentence
        for word in words_in_sentence:
            # Check if the word is in the word list and its length is greater than the current max length
            if word in self.word_list and len(word) > max_length:
                # Update the longest word and its length
                longest_word = word
                max_length = len(word)
        
        # Return the longest word, or an empty string if the word list is empty
        return longest_word