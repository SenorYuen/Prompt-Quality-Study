import re

class SplitSentence:
    def __init__(self):
        pass

    def split_sentences(self, sentences_string):
        sentences = re.split(r'(?<=[.?\s])\s*(?=[A-Z][a-z]|Mr\.|Mrs\.|Ms\.|Dr\.|Prof\.)', sentences_string)
        return [sentence for sentence in sentences if sentence]

    def count_words(self, sentence):
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        sentences = self.split_sentences(sentences_string)
        max_word_count = 0
        for sentence in sentences:
            word_count = self.count_words(sentence)
            if word_count > max_word_count:
                max_word_count = word_count
        return max_word_count