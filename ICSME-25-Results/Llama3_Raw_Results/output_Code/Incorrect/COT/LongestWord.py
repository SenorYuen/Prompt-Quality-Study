import re
import string

class LongestWord:
    # Constructor to initialize the word list
    def __init__(self):
        # Initialize an empty list to store words
        self.word_list = []

    # Method to add a word to the word list
    def add_word(self, word):
        # Append the input word to the word list
        self.word_list.append(word)

    # Method to find the longest word in a sentence that is in the word list
    def find_longest_word(self, sentence):
        # Remove punctuation marks from the sentence
        sentence_no_punct = re.sub('['+string.punctuation+']', '', sentence)
        
        # Split the sentence into a list of words
        words_in_sentence = sentence_no_punct.split()
        
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
        
        # Return the longest word that is in the word list, or an empty string if the word list is empty
        return longest_word if self.word_list else ''