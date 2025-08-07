import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    """
    This is a class about Lemmatization, which utilizes the nltk library to perform lemmatization and part-of-speech tagging on sentences, as well as remove punctuation.
    """

    def __init__(self):
        """
        Creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        """
        # Remove punctuation from the sentence
        sentence = self.remove_punctuation(sentence)
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        # Get part-of-speech tags for each word
        pos_tags = pos_tag(words)
        # Lemmatize each word based on its POS tag
        lemmatized_words = [self.lemmatizer.lemmatize(word, self.get_wordnet_pos(tag)) for word, tag in pos_tags]
        return lemmatized_words

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        """
        # Remove punctuation from the sentence
        sentence = self.remove_punctuation(sentence)
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        # Get part-of-speech tags for each word
        pos_tags = pos_tag(words)
        # Extract and return the POS tags
        return [tag for _, tag in pos_tags]

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        # Use a translation table to remove punctuation
        return sentence.translate(str.maketrans('', '', string.punctuation))

    def get_wordnet_pos(self, treebank_tag):
        """
        Convert Treebank POS tags to WordNet POS tags.
        :param treebank_tag: POS tag from pos_tag
        :return: WordNet POS tag compatible with lemmatizer
        """
        if treebank_tag.startswith('J'):
            return nltk.corpus.wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return nltk.corpus.wordnet.VERB
        elif treebank_tag.startswith('N'):
            return nltk.corpus.wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return nltk.corpus.wordnet.ADV
        else:
            return nltk.corpus.wordnet.NOUN