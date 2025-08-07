class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively
        """
        # Split the input text by spaces to separate chords and tunes
        elements = self.play_text.split()
        
        # Initialize a list to store the interpreted chords and tunes
        interpreted_music = []
        
        # Iterate over each element to determine if it's a chord or a tune
        for element in elements:
            # Assume chords are alphabetical and tunes are numerical
            if element.isalpha():
                interpreted_music.append({'Chord': element, 'Tune': None})
            elif element.isdigit():
                # In case the tune follows a chord, update the last chord with this tune
                if interpreted_music and interpreted_music[-1]['Tune'] is None:
                    interpreted_music[-1]['Tune'] = element
                else:
                    interpreted_music.append({'Chord': None, 'Tune': element})
        
        # If display is True, print out each chord and tune using the display method
        if display:
            for music in interpreted_music:
                self.display(music['Chord'], music['Tune'])
        
        return interpreted_music

    def display(self, chord, tune):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :return: str
        """
        # Format the output string based on the presence of chord and tune
        chord_str = f"Chord: {chord}" if chord else "Chord: None"
        tune_str = f"Play Tune: {tune}" if tune else "Play Tune: None"
        
        # Print the formatted string
        print(f"Normal Guitar Playing -- {chord_str}, {tune_str}")