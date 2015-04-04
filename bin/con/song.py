class SongFile:

    def __init__(self, songId, title, artist):
        self.title = title
        self.artist = artist
        self.songId = songId


    def __str__(self):
        return str(self.songId) + ": " + self.title + " by " + self.artist


class CentralStore:

    def __init__(self, song_list):
        self.song_list = song_list