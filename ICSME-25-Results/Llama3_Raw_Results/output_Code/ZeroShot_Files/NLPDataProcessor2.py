import re
from collections import Counter

class NLPDataProcessor2:

    def process_data(self, string_list):
        # Initialize an empty list to store the list of words
        words_list = []
        
        # Iterate over each string in the string list
        for string in string_list:
            # Keep only English letters and spaces in the string
            cleaned_string = re.sub(r'[^a-zA-Z\s]', '', string)
            
            # Convert the string to lower case
            cleaned_string = cleaned_string.lower()
            
            # Split the string into a list of words
            words = cleaned_string.split()
            
            # Add the list of words to the words list
            words_list.append(words)
        
        # Return the list of words
        return words_list

    def calculate_word_frequency(self, words_list):
        # Initialize an empty list to store all words
        all_words = []
        
        # Flatten the list of words into a single list
        for words in words_list:
            all_words.extend(words)
        
        # Calculate the word frequency of each word
        word_frequency = Counter(all_words)
        
        # Sort the word frequency dictionary by value in descending order
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))
        
        # Get the top 5 most frequent words
        top_5_word_frequency = dict(list(sorted_word_frequency.items())[:5])
        
        # Return the top 5 word frequency dictionary
        return top_5_word_frequency

    def process(self, string_list):
        # Process the data
        words_list = self.process_data(string_list)
        
        # Calculate the word frequency
        top_5_word_frequency = self.calculate_word_frequency(words_list)
        
        # Return the top 5 word frequency dictionary
        return top_5_word_frequency

# Example usage:
nlp_data_processor = NLPDataProcessor2()
string_list = ["This is a test string.", "This string is another test.", "Test string for NLP."]
print(nlp_data_processor.process(string_list))