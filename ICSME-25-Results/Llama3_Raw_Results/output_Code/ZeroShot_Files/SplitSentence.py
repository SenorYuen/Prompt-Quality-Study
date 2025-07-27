import re

class SplitSentence:

    def split_sentences(self, sentences_string):
        # Use regular expression to split sentences, considering Mr., Mrs., etc.
        sentences = re.split(r'(?<=[.!?]) +', sentences_string)
        # Remove leading and trailing spaces from each sentence
        sentences = [sentence.strip() for sentence in sentences]
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence]
        return sentences

    def count_words(self, sentence):
        # Remove punctuation marks and numbers, then split the sentence into words
        words = re.sub(r'[^\w\s]|[\d_]', '', sentence).split()
        # Return the number of words in the sentence
        return len(words)

    def process_text_file(self, text):
        # Split the text into sentences
        sentences = self.split_sentences(text)
        # Initialize the maximum word count
        max_word_count = 0
        # Iterate over each sentence
        for sentence in sentences:
            # Count the words in the current sentence
            word_count = self.count_words(sentence)
            # Update the maximum word count if necessary
            if word_count > max_word_count:
                max_word_count = word_count
        # Return the maximum word count
        return max_word_count