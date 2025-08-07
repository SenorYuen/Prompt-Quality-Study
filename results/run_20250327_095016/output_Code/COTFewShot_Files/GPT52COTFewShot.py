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
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        pos_tags = pos_tag(words)
        lemmatized_words = []
        for word, tag in pos_tags:
            pos = self.get_wordnet_pos(tag)
            if pos:
                lemmatized_words.append(self.lemmatizer.lemmatize(word, pos))
            else:
                lemmatized_words.append(word)
        return lemmatized_words

    def get_pos_tag(self, sentence):
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        pos_tags = pos_tag(words)
        return [tag for word, tag in pos_tags]

    def remove_punctuation(self, sentence):
        return sentence.translate(str.maketrans('', '', string.punctuation))

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return nltk.corpus.wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return nltk.corpus.wordnet.VERB
        elif treebank_tag.startswith('N'):
            return nltk.corpus.wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return nltk.corpus.wordnet.ADV
        else:
            return None