class SongFile:

    def __init__(self, songId, artist, title):
        self.artist = artist
        self.title = title
        self.songId = songId


    def __str__(self):
        return str(self.songId) + ": " + self.title + " by " + self.artist


class CentralStore:

    def __init__(self, song_list):
        #for sorting and print
        self.song_list = song_list

        # song_dic:
        # hashtable (SongFile.songId, SongFile) <- O(1)
        self.song_dic = {}
        for song in self.song_list:
            self.song_dic[song.songId] = song


    def sort_by_artist(self):
        self.song_list.sort(key=lambda x: x.artist)
        self.print_song_list()


    def sort_by_songId(self):
        self.song_list.sort(key=lambda x: x.songId)
        self.print_song_list()


    def sort_by_title(self):
        self.song_list.sort(key=lambda x: x.title)
        self.print_song_list()


    def print_song_list(self):
        for song in self.song_list:
            print song


if __name__ == "__main__":
    from bin.ctrl.rw import load_song_list

    tmp_song_list = load_song_list("SongList.txt")

    central_store = CentralStore(tmp_song_list)

    central_store.sort_by_title()
    print
    central_store.sort_by_artist()
    print
    central_store.sort_by_songId()

