import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. 
        Please note that Mr. also ends with . but are not sentences.
        :param sentences_string: string, string to split
        :return: list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        # Use regex to split sentences, considering punctuation followed by a space
        # Negative lookbehind to ensure "Mr." is not treated as a sentence end
        sentences = re.split(r'(?<!Mr)(?<=\.|\?)\s', sentences_string)
        return sentences

    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks 
        and numbers are not counted as words.
        :param sentence: string, sentence to be counted, where words are separated by spaces
        :return: int, number of words in the sentence
        >>> ss = SplitSentence()
        >>> ss.count_words("abc def")
        2
        """
        # Use regex to find all words, which are sequences of alphabetic characters
        words = re.findall(r'\b[a-zA-Z]+\b', sentence)
        return len(words)

    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return: int, the number of words in the longest sentence
        >>> ss = SplitSentence()
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        # Split the text into sentences
        sentences = self.split_sentences(sentences_string)
        # Calculate the word count for each sentence
        word_counts = [self.count_words(sentence) for sentence in sentences]
        # Return the maximum word count found
        return max(word_counts)