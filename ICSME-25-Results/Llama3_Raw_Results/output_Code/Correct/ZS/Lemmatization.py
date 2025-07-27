import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
import string

# Download required NLTK resources
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

class Lemmatization:
    def __init__(self):
        # Create a WordNetLemmatizer object
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        # Remove punctuation from the sentence
        sentence_no_punct = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence_no_punct)
        
        # Get part of speech tags for each word
        pos_tags = self.get_pos_tag(sentence_no_punct)
        
        # Initialize an empty list to store lemmatized words
        lemmatized_words = []
        
        # Map part of speech tags to WordNet tags
        for word, pos in zip(tokens, pos_tags):
            # Convert NLTK pos tag to WordNet tag
            if pos.startswith('J'):
                wordnet_pos = 'a'  # Adjective
            elif pos.startswith('V'):
                wordnet_pos = 'v'  # Verb
            elif pos.startswith('N'):
                wordnet_pos = 'n'  # Noun
            elif pos.startswith('R'):
                wordnet_pos = 'r'  # Adverb
            else:
                wordnet_pos = 'n'  # Default to noun
            
            # Lemmatize the word
            lemmatized_word = self.lemmatizer.lemmatize(word, wordnet_pos)
            
            # Add the lemmatized word to the list
            lemmatized_words.append(lemmatized_word)
        
        return lemmatized_words

    def get_pos_tag(self, sentence):
        # Remove punctuation from the sentence
        sentence_no_punct = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence_no_punct)
        
        # Get part of speech tags for each word
        pos_tags = pos_tag(tokens)
        
        # Return a list of part of speech tags
        return [pos[1] for pos in pos_tags]

    def remove_punctuation(self, sentence):
        # Use string translation to remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        return sentence.translate(translator)