class AutomaticGuitarSimulator:
    def __init__(self, text):
        """
        Initialize the score to be played.
        
        Args:
            text (str): The score to be played.
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played.
        
        Args:
            display (bool): Whether to print the interpreted score.
        
        Returns:
            list: A list of dictionaries containing the chord and tune.
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
            
            # Add the interpreted note to the list
            interpreted_notes.append({'Chord': chord, 'Tune': tune})
        
        # If display is True, print the interpreted notes
        if display:
            for note in interpreted_notes:
                print(f"Normal Guitar Playing -- Chord: {note['Chord']}, Play Tune: {note['Tune']}")
        
        # Return the list of interpreted notes
        return interpreted_notes

    def display(self, key, value):
        """
        Print out chord and play tune.
        
        Args:
            key (str): The chord.
            value (str): The tune.
        
        Returns:
            str: A string representing the chord and tune.
        """
        # Return a string representing the chord and tune
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"