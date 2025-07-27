class MusicPlayer:
    """
    This is a class as a music player that provides to play, stop, add songs, remove songs, set volume, shuffle, and switch to the next or previous song.
    """

    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
        self.playlist = []
        self.current_song = None
        self.volume = 50

    # Add a song to the playlist
    def add_song(self, song):
        """
        Adds a song to the playlist.
        :param song: The song to add to the playlist, str.
        """
        # Check if the song is already in the playlist
        if song not in self.playlist:
            # Add the song to the playlist
            self.playlist.append(song)
        # If the playlist was empty, set the current song to the newly added song
        if len(self.playlist) == 1:
            self.current_song = self.playlist[0]

    # Remove a song from the playlist
    def remove_song(self, song):
        """
        Removes a song from the playlist.
        :param song: The song to remove from the playlist, str.
        """
        # Check if the song is in the playlist
        if song in self.playlist:
            # Remove the song from the playlist
            self.playlist.remove(song)
            # If the removed song was the current song, update the current song
            if self.current_song == song:
                # If the playlist is not empty, set the current song to the first song
                if self.playlist:
                    self.current_song = self.playlist[0]
                # If the playlist is empty, set the current song to None
                else:
                    self.current_song = None

    # Play the current song in the playlist
    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        """
        # Check if there is a current song
        if self.current_song:
            # Return the current song
            return self.current_song
        # If there is no current song, return False
        else:
            return False

    # Stop the current song in the playlist
    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        # Check if there is a current song
        if self.current_song:
            # Set the current song to None
            self.current_song = None
            # Return True
            return True
        # If there is no current song, return False
        else:
            return False

    # Switch to the next song in the playlist
    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """
        # Check if there is a current song
        if self.current_song:
            # Get the index of the current song in the playlist
            current_index = self.playlist.index(self.current_song)
            # Check if there is a next song
            if current_index < len(self.playlist) - 1:
                # Set the current song to the next song
                self.current_song = self.playlist[current_index + 1]
                # Return True
                return True
            # If there is no next song, return False
            else:
                return False
        # If there is no current song, return False
        else:
            return False

    # Switch to the previous song in the playlist
    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        # Check if there is a current song
        if self.current_song:
            # Get the index of the current song in the playlist
            current_index = self.playlist.index(self.current_song)
            # Check if there is a previous song
            if current_index > 0:
                # Set the current song to the previous song
                self.current_song = self.playlist[current_index - 1]
                # Return True
                return True
            # If there is no previous song, return False
            else:
                return False
        # If there is no current song, return False
        else:
            return False

    # Set the volume of the music player
    def set_volume(self, volume):
        """
        Sets the volume of the music player,ifthe volume is between 0 and 100 is valid.
        :param volume: The volume to set the music player to,int.
        :return: True if the volume was set, False if the volume was invalid.
        """
        # Check if the volume is between 0 and 100
        if 0 <= volume <= 100:
            # Set the volume
            self.volume = volume
            # Return True
            return True
        # If the volume is invalid, return False
        else:
            return False

    # Shuffle the playlist
    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        # Check if the playlist is not empty
        if self.playlist:
            # Shuffle the playlist
            import random
            random.shuffle(self.playlist)
            # Set the current song to the first song in the shuffled playlist
            self.current_song = self.playlist[0]
            # Return True
            return True
        # If the playlist is empty, return False
        else:
            return False