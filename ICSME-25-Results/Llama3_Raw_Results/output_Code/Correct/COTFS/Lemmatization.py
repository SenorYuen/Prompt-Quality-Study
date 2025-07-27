import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    def __init__(self):
        # Create a WordNetLemmatizer object and store it
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        # Remove punctuation from the sentence
        sentence_no_punct = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence_no_punct)
        
        # Get the part of speech tag for each word
        pos_tags = pos_tag(tokens)
        
        # Lemmatize the words based on their parts of speech
        lemmatized_words = []
        for word, pos in pos_tags:
            if pos.startswith('J'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
            elif pos.startswith('V'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
            elif pos.startswith('N'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='n')
            elif pos.startswith('R'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='r')
            else:
                lemmatized_word = word
            lemmatized_words.append(lemmatized_word)
        
        return lemmatized_words

    def get_pos_tag(self, sentence):
        # Remove punctuation from the sentence
        sentence_no_punct = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence_no_punct)
        
        # Get the part of speech tag for each word
        pos_tags = pos_tag(tokens)
        
        # Return the part of speech tags
        return [pos[1] for pos in pos_tags]

    def remove_punctuation(self, sentence):
        # Remove punctuation from the sentence
        translator = str.maketrans('', '', string.punctuation)
        sentence_no_punct = sentence.translate(translator)
        
        return sentence_no_punct