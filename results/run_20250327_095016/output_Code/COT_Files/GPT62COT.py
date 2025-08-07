class NLPDataProcessor:
    
    def construct_stop_word_list(self):
        # Construct a stop word list including 'a', 'an', 'the'
        return ['a', 'an', 'the']
    
    def remove_stop_words(self, string_list, stop_word_list):
        # Remove all the stop words from the list of strings
        result = []
        for sentence in string_list:
            words = sentence.split()
            filtered_words = [word for word in words if word.lower() not in stop_word_list]
            result.append(filtered_words)
        return result
    
    def process(self, string_list):
        # Construct a stop word list and remove all the stop words from the list of strings
        stop_word_list = self.construct_stop_word_list()
        return self.remove_stop_words(string_list, stop_word_list)