'''
# This is a class about Lemmatization, which utilizes the nltk library to perform lemmatization and part-of-speech tagging on sentences, as well as remove punctuation.

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string


nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    def __init__(self):
        """
        creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """

    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :return: a list of words which have been lemmatized.
        """

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :return: list, part of speech tag of each word in the sentence.
        """

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :return: str, sentence without any punctuation

        """
'''

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')


class Lemmatization:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        lemmatized_words = []
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for word, tag in tagged_words:
            if tag.startswith('V'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
            elif tag.startswith('J'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
            elif tag.startswith('R'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='r')
            else:
                lemmatized_word = self.lemmatizer.lemmatize(word)
            lemmatized_words.append(lemmatized_word)
        return lemmatized_words

    def get_pos_tag(self, sentence):
        pos_tags = []
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for tagged_word in tagged_words:
            pos_tags.append(tagged_word[1])
        return pos_tags

    def remove_punctuation(self, sentence):
        return sentence.translate(str.maketrans('', '', string.punctuation))