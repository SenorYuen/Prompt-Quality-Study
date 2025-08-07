'''
# The class processes NLP data by removing stop words from a list of strings using a pre-defined stop word list.

class NLPDataProcessor:

    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        """
    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :return: a list of words without stop words
        """
    def process(self, string_list):
        """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :return: a list of words without stop words
        """


'''


class NLPDataProcessor:

    def construct_stop_word_list(self):
        stop_word_list = ['a', 'an', 'the']
        return stop_word_list

    def remove_stop_words(self, string_list, stop_word_list):
        answer = []
        for string in string_list:
            string_split = string.split()
            for word in string_split:
                if word in stop_word_list:
                    string_split.remove(word)
            answer.append(string_split)
        return answer

    def process(self, string_list):
        stop_word_list = self.construct_stop_word_list()
        words_list = self.remove_stop_words(string_list, stop_word_list)
        return words_list
