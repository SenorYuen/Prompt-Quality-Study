class NLPDataProcessor:
    def __init__(self):
        pass

    def construct_stop_word_list(self):
        # This method constructs a stop word list including 'a', 'an', 'the'.
        stop_word_list = ['a', 'an', 'the']
        return stop_word_list

    def remove_stop_words(self, string_list, stop_word_list):
        # This method removes all the stop words from the list of strings.
        result = []
        for string in string_list:
            words = string.split()
            words_without_stop_words = [word for word in words if word.lower() not in stop_word_list]
            result.append(words_without_stop_words)
        return result

    def process(self, string_list):
        # This method constructs a stop word list including 'a', 'an', 'the', and removes all the stop words from the list of strings.
        stop_word_list = self.construct_stop_word_list()
        return self.remove_stop_words(string_list, stop_word_list)