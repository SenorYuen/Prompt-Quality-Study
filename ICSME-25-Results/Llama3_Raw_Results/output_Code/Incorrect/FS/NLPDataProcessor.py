class NLPDataProcessor:
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """

    def construct_stop_word_list(self):
        # Construct a stop word list including 'a', 'an', 'the'
        return ['a', 'an', 'the']

    def remove_stop_words(self, string_list, stop_word_list):
        # Remove all the stop words from the list of strings
        processed_list = []
        for string in string_list:
            # Split the string into words
            words = string.split()
            # Filter out stop words
            filtered_words = [word for word in words if word.lower() not in stop_word_list]
            # Join the filtered words back into a string
            processed_string = ' '.join(filtered_words)
            # Split the processed string into words and add to the list
            processed_list.append(processed_string.split())
        return processed_list

    def process(self, string_list):
        # Construct a stop word list including 'a', 'an', 'the'
        stop_word_list = self.construct_stop_word_list()
        # Remove all the stop words from the list of strings
        return self.remove_stop_words(string_list, stop_word_list)