class AutomaticGuitarSimulator:
    """
    This class is an automatic guitar simulator that can interpret and play based on the input guitar sheet music.
    """

    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return:list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
        # Split the input text by spaces to separate each chord-tune pair
        items = self.play_text.split()
        # Initialize an empty list to store the interpreted music score
        play_list = []
        
        for item in items:
            # Find the first digit in the string to separate chord and tune
            for index, char in enumerate(item):
                if char.isdigit():
                    # Chord is the substring before the first digit
                    chord = item[:index]
                    # Tune is the substring starting from the first digit
                    tune = item[index:]
                    # Add the chord and tune as a dictionary to the play_list
                    play_list.append({'Chord': chord, 'Tune': tune})
                    break
        
        # If display is True, print each chord and tune using the display method
        if display:
            for chord_tune in play_list:
                self.display(chord_tune['Chord'], chord_tune['Tune'])
        
        return play_list

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323
        """
        # Format and print the chord and tune information
        print(f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}")