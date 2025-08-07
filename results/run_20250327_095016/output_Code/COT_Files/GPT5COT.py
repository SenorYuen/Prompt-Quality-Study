class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text

    def interpret(self, display=False):
        play_list = []
        parts = self.play_text.split()
        for part in parts:
            chord = ''.join(filter(str.isalpha, part))
            tune = ''.join(filter(str.isdigit, part))
            play_list.append({'Chord': chord, 'Tune': tune})
            if display:
                self.display(chord, tune)
        return play_list

    def display(self, key, value):
        return f"Normal Guitar Playing -- Chord: {key}, Play Tune: {value}"