class MusicPlayer:
    # Constructor to initialize the music player
    def __init__(self):
        # Initialize the playlist as an empty list
        self.playlist = []
        # Initialize the current song as None
        self.current_song = None
        # Initialize the volume to 50
        self.volume = 50

    # Method to add a song to the playlist
    def add_song(self, song):
        # Add the song to the playlist
        self.playlist.append(song)
        # If the playlist had no songs, set the current song to the newly added song
        if len(self.playlist) == 1:
            self.current_song = song

    # Method to remove a song from the playlist
    def remove_song(self, song):
        # Check if the song is in the playlist
        if song in self.playlist:
            # Remove the song from the playlist
            self.playlist.remove(song)
            # If the removed song was the current song, update the current song
            if song == self.current_song:
                # If the playlist is not empty, set the current song to the first song
                if self.playlist:
                    self.current_song = self.playlist[0]
                # If the playlist is empty, set the current song to None
                else:
                    self.current_song = None

    # Method to play the current song
    def play(self):
        # Return the current song if it exists, otherwise return False
        return self.current_song if self.current_song else False

    # Method to stop the current song
    def stop(self):
        # If there is a current song, stop it and return True
        if self.current_song:
            self.current_song = None
            return True
        # If there is no current song, return False
        else:
            return False

    # Method to switch to the next song
    def switch_song(self):
        # Check if there is a current song
        if self.current_song:
            # Find the index of the current song in the playlist
            current_index = self.playlist.index(self.current_song)
            # Check if there is a next song
            if current_index < len(self.playlist) - 1:
                # Switch to the next song
                self.current_song = self.playlist[current_index + 1]
                return True
            # If there is no next song, return False
            else:
                return False
        # If there is no current song, return False
        else:
            return False

    # Method to switch to the previous song
    def previous_song(self):
        # Check if there is a current song
        if self.current_song:
            # Find the index of the current song in the playlist
            current_index = self.playlist.index(self.current_song)
            # Check if there is a previous song
            if current_index > 0:
                # Switch to the previous song
                self.current_song = self.playlist[current_index - 1]
                return True
            # If there is no previous song, return False
            else:
                return False
        # If there is no current song, return False
        else:
            return False

    # Method to set the volume
    def set_volume(self, volume):
        # Check if the volume is between 0 and 100
        if 0 <= volume <= 100:
            # Set the volume
            self.volume = volume
            return True
        # If the volume is invalid, return False
        else:
            return False

    # Method to shuffle the playlist
    def shuffle(self):
        # Check if the playlist is not empty
        if self.playlist:
            # Shuffle the playlist
            import random
            random.shuffle(self.playlist)
            # Update the current song to the first song in the shuffled playlist
            self.current_song = self.playlist[0]
            return True
        # If the playlist is empty, return False
        else:
            return False