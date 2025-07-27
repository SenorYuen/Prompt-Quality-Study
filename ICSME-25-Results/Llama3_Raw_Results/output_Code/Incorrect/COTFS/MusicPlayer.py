class MusicPlayer:
    def __init__(self):
        # Initialize the music player with an empty playlist, no current song, and a default volume of 50.
        self.playlist = []
        self.current_song = None
        self.volume = 50

    def add_song(self, song):
        # Add a song to the playlist.
        self.playlist.append(song)

    def remove_song(self, song):
        # Remove a song from the playlist if it exists.
        if song in self.playlist:
            self.playlist.remove(song)

    def play(self):
        # Play the current song in the playlist.
        if self.current_song is not None:
            return self.current_song
        else:
            return False

    def stop(self):
        # Stop the current song in the playlist.
        if self.current_song is not None:
            self.current_song = None
            return True
        else:
            return False

    def switch_song(self):
        # Switch to the next song in the playlist.
        if self.current_song is not None:
            current_index = self.playlist.index(self.current_song)
            if current_index < len(self.playlist) - 1:
                self.current_song = self.playlist[current_index + 1]
                return True
            else:
                return False
        else:
            if len(self.playlist) > 0:
                self.current_song = self.playlist[0]
                return True
            else:
                return False

    def previous_song(self):
        # Switch to the previous song in the playlist.
        if self.current_song is not None:
            current_index = self.playlist.index(self.current_song)
            if current_index > 0:
                self.current_song = self.playlist[current_index - 1]
                return True
            else:
                return False
        else:
            return False

    def set_volume(self, volume):
        # Set the volume of the music player if it's between 0 and 100.
        if 0 <= volume <= 100:
            self.volume = volume
            return True
        else:
            return False

    def shuffle(self):
        # Shuffle the playlist.
        if len(self.playlist) > 0:
            import random
            random.shuffle(self.playlist)
            return True
        else:
            return False