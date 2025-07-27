import re
import string

class LongestWord:
    def __init__(self):
        self.word_list = []

    def add_word(self, word: str):
        self.word_list.append(word)

    def find_longest_word(self, sentence: str) -> str:
        if not self.word_list:
            return ''
        
        # Remove punctuation and split the sentence into words
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        words = sentence.split()
        
        # Find the longest word in the word list
        longest_word = ''
        for word in words:
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
                
        return longest_word