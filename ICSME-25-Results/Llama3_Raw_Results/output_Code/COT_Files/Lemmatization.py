import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

# Download required NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    def __init__(self):
        # Create a WordNetLemmatizer object and store it in the self.lemmatizer member variable
        self.lemmatizer = WordNetLemmatizer()

    def remove_punctuation(self, sentence):
        # Remove punctuation from the input text
        return sentence.translate(str.maketrans('', '', string.punctuation))

    def get_pos_tag(self, sentence):
        # Remove punctuations of the sentence
        sentence_without_punctuation = self.remove_punctuation(sentence)
        
        # Tokenize the input sentence
        tokens = word_tokenize(sentence_without_punctuation)
        
        # Mark the part of speech tag of each word
        pos_tags = pos_tag(tokens)
        
        # Return part of speech tag of each word in the sentence as list
        return [tag[1] for tag in pos_tags]

    def lemmatize_sentence(self, sentence):
        # Remove punctuations of the sentence
        sentence_without_punctuation = self.remove_punctuation(sentence)
        
        # Tokenize the input sentence
        tokens = word_tokenize(sentence_without_punctuation)
        
        # Mark the part of speech tag of each word
        pos_tags = pos_tag(tokens)
        
        # Lemmatize the words with different parameters based on their parts of speech
        lemmatized_words = []
        for word, tag in pos_tags:
            if tag.startswith('J'):
                lemmatized_word = self.lemmatizer.lemmatize(word, 'a')
            elif tag.startswith('V'):
                lemmatized_word = self.lemmatizer.lemmatize(word, 'v')
            elif tag.startswith('N'):
                lemmatized_word = self.lemmatizer.lemmatize(word, 'n')
            elif tag.startswith('R'):
                lemmatized_word = self.lemmatizer.lemmatize(word, 'r')
            else:
                lemmatized_word = word
            lemmatized_words.append(lemmatized_word)
        
        # Return a list of words which have been lemmatized
        return lemmatized_words