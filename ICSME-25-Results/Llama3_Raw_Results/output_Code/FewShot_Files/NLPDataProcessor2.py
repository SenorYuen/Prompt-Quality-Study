import re
from collections import Counter

class NLPDataProcessor2:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    # Method to process the data by removing non-English characters, converting to lower case, and splitting into words
    def process_data(self, string_list):
        # Initialize an empty list to store the processed words
        words_list = []
        # Iterate over each string in the input list
        for string in string_list:
            # Remove non-English characters and convert to lower case
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            # Split the string into words and add to the list
            words_list.append(cleaned_string.split())
        return words_list

    # Method to calculate the word frequency of each word in the list of words
    def calculate_word_frequency(self, words_list):
        # Flatten the list of words lists into a single list of words
        flat_words_list = [word for sublist in words_list for word in sublist]
        # Calculate the word frequency using Counter
        word_frequency = Counter(flat_words_list)
        # Sort the word frequency dictionary by value in descending order and return the top 5
        return dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)[:5])

    # Method to process the data and calculate the word frequency
    def process(self, string_list):
        # Process the data using the process_data method
        words_list = self.process_data(string_list)
        # Calculate the word frequency using the calculate_word_frequency method
        word_frequency = self.calculate_word_frequency(words_list)
        return word_frequency