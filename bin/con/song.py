class SongFile:

    def __init__(self, songId, title, artist):
        self.title = title
        self.artist = artist
        self.songId = songId


    def __str__(self):
        return str(self.songId) + ": " + self.title + " by " + self.artist


class CentralStore:

    def __init__(self, song_list):
        # song_dic:
        # hashtable (SongFile.songId, SongFile) <- O(1)
        self.song_dic = {}
        for song in song_list:
            self.song_dic[song.songId] = song

    