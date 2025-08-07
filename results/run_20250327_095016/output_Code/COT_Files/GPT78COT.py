import re

class SplitSentence:
    def split_sentences(self, sentences_string):
        sentences = re.split(r'(?<!\bMr)(?<!\bMrs)(?<!\bMs)(?<!\bDr)(?<!\bJr)\.\s|\?\s', sentences_string)
        sentences = [s.strip() for s in sentences if s]
        return sentences

    def count_words(self, sentence):
        words = re.findall(r'\b\w+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        sentences = self.split_sentences(sentences_string)
        max_word_count = max(self.count_words(sentence) for sentence in sentences)
        return max_word_count