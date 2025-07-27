import re
from collections import Counter

class NLPDataProcessor2:
    """
    The class processes NLP data by extracting words from a list of strings, calculating the frequency of each word, and returning the top 5 most frequent words.
    """

    def process_data(self, string_list):
        """
        Keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        """
        # Initialize an empty list to store lists of words
        words_list = []
        
        # Iterate over each string in the input list
        for string in string_list:
            # Use regex to remove non-letter characters and convert to lowercase
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            # Split the cleaned string into words and append to words_list
            words_list.append(cleaned_string.split())
        
        return words_list

    def calculate_word_frequency(self, words_list):
        """
        Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param words_list: a list of words lists
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        # Flatten the list of lists into a single list of words
        all_words = [word for sublist in words_list for word in sublist]
        
        # Use Counter to count the frequency of each word
        word_count = Counter(all_words)
        
        # Get the 5 most common words and their frequencies
        most_common_words = word_count.most_common(5)
        
        # Convert the list of tuples into a dictionary
        return dict(most_common_words)

    def process(self, string_list):
        """
        Keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        """
        # Process the input strings to get a list of words lists
        words_list = self.process_data(string_list)
        
        # Calculate and return the word frequency dictionary
        return self.calculate_word_frequency(words_list)