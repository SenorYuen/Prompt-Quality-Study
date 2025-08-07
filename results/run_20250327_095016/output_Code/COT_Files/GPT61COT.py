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

    def play(self):
        if self.current_song in self.playlist:
            return self.current_song
        return False

    def stop(self):
        if self.current_song:
            self.current_song = None
            return True
        return False

    def switch_song(self):
        if self.current_song in self.playlist:
            index = self.playlist.index(self.current_song)
            if index + 1 < len(self.playlist):
                self.current_song = self.playlist[index + 1]
                return True
        return False

    def previous_song(self):
        if self.current_song in self.playlist:
            index = self.playlist.index(self.current_song)
            if index > 0:
                self.current_song = self.playlist[index - 1]
                return True
        return False

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            return True
        return False

    def shuffle(self):
        if self.playlist:
            import random
            random.shuffle(self.playlist)
            return True
        return False