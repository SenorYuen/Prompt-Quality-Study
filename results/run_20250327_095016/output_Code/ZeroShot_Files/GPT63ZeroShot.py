import re
from collections import Counter

class NLPDataProcessor2:

    def process_data(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case,
        and then split the string into a list of words.
        :return: words_list: a list of words lists
        """
        # Initialize an empty list to store words
        words_list = []
        
        # Iterate over each string in the input list
        for string in string_list:
            # Use regex to keep only letters and spaces, then convert to lower case
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            # Split the cleaned string into words and extend the words_list
            words_list.extend(cleaned_string.split())
        
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list,
        and sort the word frequency dictionary by value in descending order.
        :return: top 5 word frequency dictionary, a dictionary of word frequency,
        key is word, value is frequency
        """
        # Use Counter to calculate word frequencies
        word_count = Counter(words_list)
        # Get the 5 most common words and their frequencies
        top_5_words = word_count.most_common(5)
        # Convert the list of tuples to a dictionary
        top_5_word_dict = dict(top_5_words)
        
        return top_5_word_dict

    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case,
        and then split the string into a list of words. Calculate the word frequency of each word
        in the list of words list, and sort the word frequency dictionary by value in descending order.
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        # Process the data to get a list of words
        words_list = self.process_data(string_list)
        # Calculate and return the top 5 word frequencies
        return self.calculate_word_frequency(words_list)