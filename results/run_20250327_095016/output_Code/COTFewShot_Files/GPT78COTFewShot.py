import re

class SplitSentence:
    def split_sentences(self, sentences_string):
        sentences = re.split(r'(?<=[.?\s])\s+', sentences_string.strip())
        return [sentence.strip() for sentence in sentences if sentence]

    def count_words(self, sentence):
        words = re.findall(r'\b\w+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        sentences = self.split_sentences(sentences_string)
        max_word_count = 0
        for sentence in sentences:
            word_count = self.count_words(sentence)
            if word_count > max_word_count:
                max_word_count = word_count
        return max_word_count