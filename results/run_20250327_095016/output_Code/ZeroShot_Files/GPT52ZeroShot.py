class Lemmatization:
    def __init__(self):
        """
        Creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Removes punctuation from the sentence, tokenizes the input sentence, marks the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores them in a list.
        :param sentence: str, the input sentence to be lemmatized
        :return: list of str, words which have been lemmatized
        """
        # Remove punctuation from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Get part of speech tags for each token
        pos_tags = pos_tag(tokens)
        
        # Lemmatize each token based on its POS tag
        lemmatized_words = []
        for word, tag in pos_tags:
            pos = self.get_wordnet_pos(tag)
            lemmatized_word = self.lemmatizer.lemmatize(word, pos)
            lemmatized_words.append(lemmatized_word)
        
        return lemmatized_words

    def get_pos_tag(self, sentence):
        """
        Removes punctuation from the sentence and tokenizes the input sentence, marks the part of speech tag of each word.
        :param sentence: str, the input sentence
        :return: list of tuples, part of speech tag of each word in the sentence
        """
        # Remove punctuation from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Return POS tags for each token
        return pos_tag(tokens)

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: str, the input sentence
        :return: str, sentence without any punctuation
        """
        # Create a translation table for removing punctuation
        translator = str.maketrans('', '', string.punctuation)
        
        # Return the sentence without punctuation
        return sentence.translate(translator)

    def get_wordnet_pos(self, treebank_tag):
        """
        Converts Treebank POS tags to WordNet POS tags.
        :param treebank_tag: str, the Treebank POS tag
        :return: str, the corresponding WordNet POS tag
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
            return nltk.corpus.wordnet.NOUN  # Default to noun if no match