class NLPDataProcessor:

    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        """
        # Define the initial stop words
        stop_words = ['a', 'an', 'the']
        return stop_words

    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :return: a list of words without stop words
        """
        # Initialize an empty list to store the result
        result = []
        # Iterate over each string in the list
        for string in string_list:
            # Split the string into words
            words = string.split()
            # Filter out the stop words
            filtered_words = [word for word in words if word.lower() not in stop_word_list]
            # Add the filtered words to the result
            result.extend(filtered_words)
        return result

    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :return: a list of words without stop words
        """
        # Construct the stop word list
        stop_word_list = self.construct_stop_word_list()
        # Remove the stop words from the string list
        result = self.remove_stop_words(string_list, stop_word_list)
        return result

# Example usage:
if __name__ == "__main__":
    processor = NLPDataProcessor()
    string_list = ["I am going to the store", "I have an apple"]
    result = processor.process(string_list)
    print(result)