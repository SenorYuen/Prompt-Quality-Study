class AutomaticGuitarSimulator:
    def __init__(self, text):
        self.play_text = text

    def interpret(self, display=False):
        score = self.play_text.split()
        interpreted_score = []

        for chord in score:
            chord_name = ''.join(filter(str.isalpha, chord))
            tune = ''.join(filter(str.isdigit, chord))
            interpreted_score.append({'Chord': chord_name, 'Tune': tune})
            if display:
                self.display(chord_name, tune)

        return interpreted_score

    def display(self, key, value):
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"