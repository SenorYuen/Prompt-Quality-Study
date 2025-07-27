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
        :return:list of dict, The dict includes two fields, Chore and Tune, which are letters and numbers, respectively
        """
        # Split the input text into individual notes
        notes = self.play_text.split()
        
        # Initialize an empty list to store the interpreted notes
        interpreted_notes = []
        
        # Iterate over each note
        for note in notes:
            # Extract the chord and tune from the note
            chord = ''
            tune = ''
            for char in note:
                if char.isalpha():
                    chord += char
                else:
                    tune += char
            
            # Create a dictionary to store the chord and tune
            note_dict = {'Chord': chord, 'Tune': tune}
            
            # Add the note dictionary to the list of interpreted notes
            interpreted_notes.append(note_dict)
        
        # If display is True, print out the interpreted notes
        if display:
            for note in interpreted_notes:
                self.display(note['Chord'], note['Tune'])
        
        # Return the list of interpreted notes
        return interpreted_notes


    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        """
        # Print out the chord and tune in the specified format
        print(f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}")