class Lemmatization:
    """
    This is a class about Lemmatization, which utilizes the nltk library to perform lemmatization and part-of-speech tagging on sentences, as well as remove punctuation.
    """

    def __init__(self):
        """
        creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        # Initialize the WordNetLemmatizer object
        self.lemmatizer = WordNetLemmatizer()

    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']

        """
        # Remove punctuation from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Get the part of speech tags for each word
        pos_tags = self.get_pos_tag(sentence)
        
        # Initialize an empty list to store the lemmatized words
        lemmatized_words = []
        
        # Iterate over each word and its corresponding part of speech tag
        for word, pos in zip(words, pos_tags):
            # Determine the part of speech tag
            if pos.startswith('J'):
                # Adjective
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
            elif pos.startswith('V'):
                # Verb
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
            elif pos.startswith('N'):
                # Noun
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='n')
            elif pos.startswith('R'):
                # Adverb
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='r')
            else:
                # Default to noun
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='n')
            
            # Add the lemmatized word to the list
            lemmatized_words.append(lemmatized_word)
        
        # Return the list of lemmatized words
        return lemmatized_words

    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']

        """
        # Remove punctuation from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Get the part of speech tags for each word
        pos_tags = pos_tag(words)
        
        # Extract the part of speech tags
        pos_tags = [tag[1] for tag in pos_tags]
        
        # Return the list of part of speech tags
        return pos_tags

    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'

        """
        # Use the translate method to remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        sentence = sentence.translate(translator)
        
        # Return the sentence without punctuation
        return sentence