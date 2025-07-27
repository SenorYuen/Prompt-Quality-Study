import random

class MusicPlayer:
    def __init__(self):
        # Initializes the music player with an empty playlist, no current song, and a default volume of 50
        self.playlist = []
        self.current_song = None
        self.volume = 50
        self.current_index = 0

    def add_song(self, song):
        # Adds a song to the playlist
        self.playlist.append(song)
        # If the playlist was empty, set the current song to the newly added song
        if len(self.playlist) == 1:
            self.current_song = song
            self.current_index = 0

    def remove_song(self, song):
        # Removes a song from the playlist
        if song in self.playlist:
            self.playlist.remove(song)
            # If the removed song was the current song, set the current song to None
            if song == self.current_song:
                self.current_song = None
                self.current_index = 0
            # If the removed song was not the current song, but was before the current song in the playlist,
            # decrement the current index to keep the current song correct
            elif self.playlist.index(song) < self.current_index:
                self.current_index -= 1

    def play(self):
        # Plays the current song in the playlist
        if self.current_song is not None:
            print(f"Playing {self.current_song} at volume {self.volume}")
            return self.current_song
        else:
            print("No song to play")
            return False

    def stop(self):
        # Stops the current song in the playlist
        if self.current_song is not None:
            print(f"Stopped {self.current_song}")
            return True
        else:
            print("No song to stop")
            return False

    def switch_song(self):
        # Switches to the next song in the playlist
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.current_song = self.playlist[self.current_index]
            print(f"Switched to {self.current_song}")
            return True
        else:
            print("No next song")
            return False

    def previous_song(self):
        # Switches to the previous song in the playlist
        if self.current_index > 0:
            self.current_index -= 1
            self.current_song = self.playlist[self.current_index]
            print(f"Switched to {self.current_song}")
            return True
        else:
            print("No previous song")
            return False

    def set_volume(self, volume):
        # Sets the volume of the music player if the volume is between 0 and 100
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"Volume set to {self.volume}")
            return True
        else:
            print("Invalid volume")
            return False

    def shuffle(self):
        # Shuffles the playlist
        if len(self.playlist) > 0:
            random.shuffle(self.playlist)
            self.current_index = 0
            self.current_song = self.playlist[self.current_index]
            print("Playlist shuffled")
            return True
        else:
            print("Playlist is empty")
            return False

# Example usage:
music_player = MusicPlayer()
music_player.add_song("Song 1")
music_player.add_song("Song 2")
music_player.add_song("Song 3")
music_player.play()
music_player.switch_song()
music_player.play()
music_player.previous_song()
music_player.play()
music_player.set_volume(75)
music_player.play()
music_player.shuffle()
music_player.play()