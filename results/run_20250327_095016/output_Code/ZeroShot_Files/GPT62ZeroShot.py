class NLPDataProcessor:

    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        """
        # Define a list of stop words
        stop_words = ['a', 'an', 'the']
        return stop_words

    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: list of strings to be processed
        :param stop_word_list: list of stop words to be removed
        :return: a list of words without stop words
        """
        # Initialize an empty list to store the result
        filtered_list = []
        
        # Iterate over each string in the input list
        for string in string_list:
            # Split the string into words
            words = string.split()
            # Filter out stop words
            filtered_words = [word for word in words if word.lower() not in stop_word_list]
            # Join the filtered words back into a string
            filtered_string = ' '.join(filtered_words)
            # Add the filtered string to the result list
            filtered_list.append(filtered_string)
        
        return filtered_list

    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: list of strings to be processed
        :return: a list of words without stop words
        """
        # Construct the stop word list
        stop_word_list = self.construct_stop_word_list()
        # Remove stop words from the input string list
        return self.remove_stop_words(string_list, stop_word_list)