class NLPDataProcessor:
    """
    The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.
    """

    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        >>> NLPDataProcessor().construct_stop_word_list()
        ['a', 'an', 'the']
        """
        # Define a list of stop words
        stop_words = ['a', 'an', 'the']
        return stop_words

    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor().remove_stop_words(['This is a test.'], ['a', 'an', 'the'])
        [['This', 'is', 'test.']]
        """
        # Initialize a list to hold the processed strings
        processed_list = []
        for sentence in string_list:
            # Split the sentence into words
            words = sentence.split()
            # Filter out stop words
            filtered_words = [word for word in words if word.lower() not in stop_word_list]
            # Append the filtered words to the processed list
            processed_list.append(filtered_words)
        return processed_list

    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        >>> NLPDataProcessor().process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        # Construct the stop word list
        stop_word_list = self.construct_stop_word_list()
        # Remove stop words from the string list
        return self.remove_stop_words(string_list, stop_word_list)