'''
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


    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :return: str
        """


'''


class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text

    def interpret(self, display=False):
        if len(self.play_text) == 0:
            return
        else:
            play_list = []
            play_segs = self.play_text.split(" ")
            for play_seg in play_segs:
                pos = 0
                for ele in play_seg:
                    if ele.isalpha():
                        pos += 1
                        continue
                    break
                play_chord = play_seg[0:pos]
                play_value = play_seg[pos:]
                play_list.append({'Chord': play_chord, 'Tune': play_value})
                if display:
                    self.display(play_chord, play_value)
            return play_list

    def display(self, key, value):
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value)


