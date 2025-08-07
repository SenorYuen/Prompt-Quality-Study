import re

class SplitSentence:

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. 
        Please note that Mr. also ends with . but are not sentences.
        :param sentences_string: str, the text to split into sentences
        :return: list, split sentence list
        """
        # Use regex to split the text into sentences, handling abbreviations like "Mr."
        # Sentences end with . or ? followed by a space, but exclude common abbreviations.
        sentence_pattern = r'(?<!\bMr)(?<!\bMrs)(?<!\bMs)(?<!\bDr)(?<!\bJr)(?<!\bSr)(?<!\bProf)(?<!\bInc)(?<!\bLtd)(?<!\bCo)(?<=[.!?]) +'
        sentences = re.split(sentence_pattern, sentences_string)
        return [sentence.strip() for sentence in sentences if sentence.strip()]

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks 
        and numbers are not counted as words.
        :param sentence: str, the sentence to count words in
        :return: int, number of words in the sentence
        """
        # Use regex to find all words, excluding punctuation and numbers
        words = re.findall(r'\b[A-Za-z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: str, the text to process
        :return: int, the number of words in the longest sentence
        """
        # Split the text into sentences
        sentences = self.split_sentences(sentences_string)
        # Calculate the word count for each sentence and find the maximum
        max_word_count = max(self.count_words(sentence) for sentence in sentences)
        return max_word_count