# This class is an automatic guitar simulator that can interpret and play based on the input guitar sheet music.

class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :return:list of dict, The dict includes two fields, Chore and Tune, which are letters and numbers, respectively
        """
        # Assuming the input text is a string of space-separated chord and tune pairs
        score = self.play_text.split(',')
        interpreted_score = []
        
        # Iterate over each pair in the score
        for pair in score:
            # Split the pair into chord and tune
            chord_tune = pair.split(':')
            
            # Check if the pair is in the correct format
            if len(chord_tune) != 2:
                raise ValueError("Invalid score format")
            
            # Extract chord and tune
            chord = chord_tune[0].strip()
            tune = chord_tune[1].strip()
            
            # Check if the tune is a number
            if not tune.isdigit():
                raise ValueError("Tune must be a number")
            
            # Create a dictionary for the chord and tune
            chord_tune_dict = {
                "Chore": chord,
                "Tune": int(tune)
            }
            
            # Add the dictionary to the interpreted score
            interpreted_score.append(chord_tune_dict)
        
        # If display is True, print out the interpreted score
        if display:
            for key, value in interpreted_score:
                self.display(key, value)
        
        return interpreted_score


    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :return: str
        """
        # Print out the chord and tune
        print("Normal Guitar Playing -- Chord: %s, Play Tune: %d" % (key, value))
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %d" % (key, value)


# Example usage:
simulator = AutomaticGuitarSimulator("A:1, B:2, C:3")
interpreted_score = simulator.interpret(display=True)