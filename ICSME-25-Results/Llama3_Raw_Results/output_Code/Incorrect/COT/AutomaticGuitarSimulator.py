class AutomaticGuitarSimulator:
    # Constructor method to initialize the score to be played
    def __init__(self, text):
        """
        Initialize the score to be played.
        
        Args:
            text (str): The score to be played.
        """
        self.play_text = text

    # Method to interpret the music score to be played
    def interpret(self, display=False):
        """
        Interpret the music score to be played.
        
        Args:
            display (bool): Whether to print the interpreted score. Defaults to False.
        
        Returns:
            list: A list of dictionaries containing the chord and tune.
        """
        # Split the input text into individual notes
        notes = self.play_text.split()
        
        # Initialize an empty list to store the interpreted notes
        play_list = []
        
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
            
            # Add the interpreted note to the list
            play_list.append({'Chord': chord, 'Tune': tune})
        
        # If display is True, print the interpreted score
        if display:
            for note in play_list:
                print(f"Normal Guitar Playing -- Chord: {note['Chord']}, Play Tune: {note['Tune']}")
        
        # Return the list of interpreted notes
        return play_list

    # Method to print out chord and play tune
    def display(self, key, value):
        """
        Print out chord and play tune.
        
        Args:
            key (str): The chord.
            value (str): The play tune.
        
        Returns:
            str: A string representing the chord and play tune.
        """
        # Return a string representing the chord and play tune
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"