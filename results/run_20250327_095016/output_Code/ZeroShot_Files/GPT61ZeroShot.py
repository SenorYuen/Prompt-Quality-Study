import random

class MusicPlayer:
    def __init__(self):
        """
        Initializes the music player with an empty playlist, no current song, and a default volume of 50.
        """
        self.playlist = []  # List to store songs
        self.current_index = -1  # Index of the current song, -1 means no song is playing
        self.volume = 50  # Default volume

    def add_song(self, song):
        """
        Adds a song to the playlist.
        """
        self.playlist.append(song)  # Append the song to the playlist

    def remove_song(self, song):
        """
        Removes a song from the playlist.
        """
        if song in self.playlist:
            self.playlist.remove(song)  # Remove the song if it exists in the playlist

    def play(self):
        """
        Plays the current song in the playlist.
        :return: The current song in the playlist, or False if there is no current song.
        """
        if self.current_index == -1 and self.playlist:
            self.current_index = 0  # Start from the first song if no song is currently playing
        if self.current_index != -1:
            return self.playlist[self.current_index]  # Return the current song
        return False

    def stop(self):
        """
        Stops the current song in the playlist.
        :return: True if the current song was stopped, False if there was no current song.
        """
        if self.current_index != -1:
            self.current_index = -1  # Stop playing by resetting the index
            return True
        return False

    def switch_song(self):
        """
        Switches to the next song in the playlist.
        :return: True if the next song was switched to, False if there was no next song.
        """
        if self.current_index != -1 and self.current_index < len(self.playlist) - 1:
            self.current_index += 1  # Move to the next song
            return True
        return False

    def previous_song(self):
        """
        Switches to the previous song in the playlist.
        :return: True if the previous song was switched to, False if there was no previous song.
        """
        if self.current_index > 0:
            self.current_index -= 1  # Move to the previous song
            return True
        return False

    def set_volume(self, volume):
        """
        Sets the volume of the music player, if the volume is between 0 and 100 is valid.
        :return: True if the volume was set, False if the volume was invalid.
        """
        if 0 <= volume <= 100:
            self.volume = volume  # Set the new volume
            return True
        return False

    def shuffle(self):
        """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        """
        if self.playlist:
            random.shuffle(self.playlist)  # Shuffle the playlist
            self.current_index = -1  # Reset the current song
            return True
        return False