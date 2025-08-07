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
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        lemmatized_words = []
        for word, tag in pos_tags:
            pos = self.get_wordnet_pos(tag)
            lemmatized_words.append(self.lemmatizer.lemmatize(word, pos))
        return lemmatized_words

    def get_pos_tag(self, sentence):
        sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        return [tag for word, tag in pos_tags]

    def remove_punctuation(self, sentence):
        return sentence.translate(str.maketrans('', '', string.punctuation))

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return 'a'  # Adjective
        elif treebank_tag.startswith('V'):
            return 'v'  # Verb
        elif treebank_tag.startswith('N'):
            return 'n'  # Noun
        elif treebank_tag.startswith('R'):
            return 'r'  # Adverb
        else:
            return 'n'  # Default to noun