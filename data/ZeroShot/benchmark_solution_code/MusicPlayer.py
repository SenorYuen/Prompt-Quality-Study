'''
# This is a class as a music player that provides to play, stop, add songs, remove songs, set volume, shuffle, and switch to the next or previous song.

class MusicPlayer:
    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
    def add_song(self, song):
        """
        Adds a song to the playlist.
        """

    def remove_song(self, song):
        """
        Removes a song from the playlist.
        """

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        """

    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """

    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """

    def set_volume(self, volume):
        """
        Sets the volume of the music player,ifthe volume is between 0 and 100 is valid.
        :return: True if the volume was set, False if the volume was invalid.
        """

    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
'''
class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = None
        self.volume = 50

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            if self.current_song == song:
                self.stop()

    def play(self):
        if self.playlist and self.current_song:
            return self.playlist[0]
        elif len(self.playlist): 
            return False

    def stop(self):
        if self.current_song:
            self.current_song = None
            return True
        else:
            return False

    def switch_song(self):
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            if current_index < len(self.playlist) - 1:
                self.current_song = self.playlist[current_index + 1]
                return True
            else:
                return False
        else:
            return False

    def previous_song(self):
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            if current_index > 0:
                self.current_song = self.playlist[current_index - 1]
                return True
            else:
                return False
        else:
            return False

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
        else:
            return False

    def shuffle(self):
        if self.playlist:
            import random
            random.shuffle(self.playlist)
            return True
        else:
            return False
