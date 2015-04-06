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
        # {SongFile.songId: SongFile}
        # hashtable <- O(1)
        self.song_dic = {}
        for song in self.song_list:
            self.song_dic[song.songId] = song

        # {playlistId: ("playlist name", [SongFile])}
        self.playlists = {}
        self.next_playlistId = 0


    def add_playlist(self, playlist_name, playlist=[]):
        self.playlists[self.next_playlistId] = (playlist_name, playlist)

        playlistId = self.next_playlistId

        self.next_playlistId += 1

        return playlistId


    def search_by_artist(self, keyword, song_list=None):
        if not song_list:
            song_list = self.song_list

        tmp_result = []

        for song in song_list:
            if keyword.lower() in song.artist.lower(): # artist name containing the keyword
            #if keyword == song.artist:  # exactly the same artist name with the keyword
            #                            # (by 'a' particular artist)
                tmp_result.append(song)

        tmp_result.sort(key=lambda x: x.title)

        return tmp_result


    def search_by_title(self, keyword, song_list=None):
        if not song_list:
            song_list = self.song_list

        tmp_result = []

        for song in song_list:
            if keyword.lower() in song.title.lower():
                tmp_result.append(song)

        tmp_result.sort(key=lambda x: x.title)

        return tmp_result


    def sort_by_artist(self, song_list=None):
        if not song_list:
            song_list = self.song_list

        song_list.sort(key=lambda x: x.artist)


    def sort_by_songId(self, song_list=None):
        if not song_list:
            song_list = self.song_list

        song_list.sort(key=lambda x: x.songId)


    def sort_by_title(self, song_list=None):
        if not song_list:
            song_list = self.song_list

        song_list.sort(key=lambda x: x.title)


    def print_song_list(self, song_list):
        print "{0:6}  {1:32}  {2:16}".format("SongId", "Title", "Artist")
        print '-'*58
        for song in song_list:
            print "{0:6}  {1:32}  {2:16}".format(song.songId, song.title, song.artist)


    def print_playlist(self, playlistId):
        print "Playlist " + str(playlistId) + ": " + self.playlists[playlistId][0]
        print '-'*62
        print "    {0:6}  {1:32}  {2:16}".format("SongId", "Title", "Artist")
        print '-'*62
        for song in self.playlists[playlistId][1]:
            print "    {0:6}  {1:32}  {2:16}".format(song.songId, song.title, song.artist)


    def print_playlists(self):
        for playlistId in self.playlists:
            self.print_playlist(playlistId)
            print


if __name__ == "__main__":
    from bin.ctrl.rw import load_song_list

    tmp_song_list = load_song_list("SongList.txt")

    central_store = CentralStore(tmp_song_list)

    central_store.print_song_list()

    #central_store.sort_by_artist(central_store.song_list)
    #print
    #central_store.sort_by_songId(central_store.song_list)
    #print
    #central_store.sort_by_title(central_store.song_list)
    #print

    #tmp_result = central_store.search_by_artist("The Doors")
    #for elem in tmp_result:
    #    print elem

    #tmp_result = central_store.search_by_title("Light")
    #for elem in tmp_result:
    #    print elem

    central_store.add_playlist("first")
    central_store.add_playlist("second")
    central_store.add_playlist("third")
    #for idx in central_store.playlists:
    #    print idx, central_store.playlists[idx]

    print

    central_store.print_playlists()