from collections import Counter
import re

class NLPDataProcessor2:
    def process_data(self, string_list):
        # Keep only English letters and spaces in the string, 
        # then convert the string to lower case, and then split the string into a list of words.
        words_list = []
        for string in string_list:
            # Remove non-English letters and convert to lower case
            cleaned_string = re.sub('[^a-zA-Z\s]', '', string).lower()
            # Split the string into a list of words
            words = cleaned_string.split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        # Calculate the word frequency of each word in the list of words list, 
        # and sort the word frequency dictionary by value in descending order.
        # Flatten the list of words lists into a single list of words
        words = [word for sublist in words_list for word in sublist]
        # Calculate the word frequency using Counter
        word_frequency = Counter(words)
        # Sort the word frequency dictionary by value in descending order and get the top 5
        top_5_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)[:5])
        return top_5_word_frequency

    def process(self, string_list):
        # Keep only English letters and spaces in the string, 
        # then convert the string to lower case, and then split the string into a list of words. 
        # Calculate the word frequency of each word in the list of words list, 
        # and sort the word frequency dictionary by value in descending order.
        words_list = self.process_data(string_list)
        top_5_word_frequency = self.calculate_word_frequency(words_list)
        return top_5_word_frequency