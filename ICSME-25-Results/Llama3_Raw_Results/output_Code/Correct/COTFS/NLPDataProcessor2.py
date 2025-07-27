from collections import Counter
import re

class NLPDataProcessor2:
    def process_data(self, string_list):
        # Keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        words_list = []
        for string in string_list:
            # Remove non-English letters and spaces, convert to lower case, and split into words
            words = re.sub('[^a-zA-Z\s]', '', string).lower().split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        # Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        word_frequency = Counter(word for words in words_list for word in words)
        # Sort the word frequency dictionary by value in descending order and return the top 5
        return dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)[:5])

    def process(self, string_list):
        # Keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. 
        # Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)