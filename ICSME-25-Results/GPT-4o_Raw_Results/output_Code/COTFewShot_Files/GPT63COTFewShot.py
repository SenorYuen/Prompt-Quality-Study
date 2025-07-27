from collections import Counter
import re

class NLPDataProcessor:
    def process_data(self, string_list):
        words_list = []
        for string in string_list:
            processed_string = re.sub(r'[^a-zA-Z\s]', '', string).lower()
            words = processed_string.split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        frequency = Counter()
        for words in words_list:
            frequency.update(words)
        return dict(frequency.most_common(5))

    def process(self, string_list):
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)