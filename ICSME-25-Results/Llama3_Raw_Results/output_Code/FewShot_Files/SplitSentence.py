import re

class SplitSentence:
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        # Use regular expression to split the string into sentences
        # The pattern matches one or more whitespace characters followed by a period or question mark
        # The period or question mark is included in the match to ensure it's not lost during splitting
        sentences = re.split('(?<=[.!?]) +', sentences_string)
        return sentences

    def count_words(self, sentence):
        # Remove punctuation marks and numbers from the sentence
        # The pattern matches one or more non-word characters (everything except alphanumeric characters and underscores)
        sentence = re.sub(r'[^\w\s]', '', sentence)
        # Split the sentence into words
        words = sentence.split()
        return len(words)

    def process_text_file(self, sentences_string):
        # Split the string into sentences
        sentences = self.split_sentences(sentences_string)
        # Initialize the maximum word count
        max_word_count = 0
        # Iterate over each sentence
        for sentence in sentences:
            # Count the words in the sentence
            word_count = self.count_words(sentence)
            # Update the maximum word count if necessary
            if word_count > max_word_count:
                max_word_count = word_count
        return max_word_count