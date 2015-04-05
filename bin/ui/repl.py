from bin.con.song import CentralStore

import sys


class REPL:

    def __init__(self, central_store):
        self.central_store = central_store

        self.curr_menu = "main" #"main", "playlist"
        self.curr_playlistId = None


    def repl(self):
        cmd_line = raw_input(self.curr_menu + "> ")

        if not cmd_line:
            return

        cmd_list = cmd_line.split()

        if self.curr_menu == "main":
            if cmd_line.startswith("create"):
                self.create(cmd_line)
            elif cmd_line.startswith("edit"):
                self.edit(cmd_line)
            elif cmd_list[0] == "playlist":
                self.playlist(cmd_list)
            elif cmd_list[0] == "print":
                self.print_list(cmd_list)
            elif cmd_line.startswith("quit"):
                self.quit(cmd_line)
            elif cmd_list[0] == "search":
                self.search(cmd_list)
            elif cmd_line.startswith("song"):
                self.song(cmd_line)
            elif cmd_list[0] == "sort":
                self.sort(cmd_list)
            else:
                print "Wrong command " + cmd_line + '.'
        elif self.curr_menu == "playlist":
            if cmd_list[0] == "delete":
                self.delete(cmd_list)
            elif cmd_list[0] == "insert":
                self.insert(cmd_list)
            elif cmd_list[0] == "insert_search":
                self.insert_search(cmd_list)
            elif cmd_line.startswith("main"):
                self.main(cmd_line)
            elif cmd_list[0] == "print":
                self.print_curr_playlist(cmd_list)
            elif cmd_list[0] == "search":
                self.search_playlist(cmd_list)
            elif cmd_list[0] == "sort":
                self.sort_playlist(cmd_list)
            else:
                print "Wrong command " + cmd_line + '.'


    def create(self, cmd_line):
        cmd_list = cmd_line.split()

        if cmd_list[0] == "create" and len(cmd_list) >= 2:
            playlistId = self.central_store.add_playlist(" ".join(cmd_list[1:]), playlist=list())

            self.curr_menu = "playlist"
            self.curr_playlistId = playlistId
        else:
            print "Wrong command " + cmd_line + '.'


    def edit(self, cmd_line):
        cmd_list = cmd_line.split()

        if cmd_list[0] == "edit" and len(cmd_list) == 2:
            try:
                playlistId = int(cmd_list[1])
                self.central_store.playlists[playlistId]

                self.curr_menu = "playlist"
                self.curr_playlistId = playlistId
            except ValueError, e:
                print "Wrong playlistId " + cmd_list[1] + "."
            except KeyError, e:
                print "Playlist " + cmd_list[1] + " doest not exist."
        else:
            print "Wrong command " + cmd_line + '.'


    def playlist(self, cmd_list):
        if len(cmd_list) == 2:
            try:
                playlistId = int(cmd_list[1])
                self.central_store.playlists[playlistId]

                self.central_store.print_playlist(playlistId)
            except ValueError, e:
                print "Wrong playlistId " + cmd_list[1] + "."
            except KeyError, e:
                print "Playlist " + cmd_list[1] + " doest not exist."
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'


    def print_list(self, cmd_list):
        if len(cmd_list) == 2:
            if cmd_list[1] == "song":
                self.central_store.print_song_list(self.central_store.song_list)
            elif cmd_list[1] == "playlist":
                self.central_store.print_playlists()
            else:
                print "Wrong option " + cmd_list[1]
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'


    def quit(self, cmd_line):
        cmd_list = cmd_line.split()

        if cmd_list[0] == "quit" and len(cmd_list) == 1:
            #python auto garbage collection
            sys.exit()
        else:
            print "Wrong command " + cmd_line + '.'


    def search(self, cmd_list):
        if len(cmd_list) == 3:
            keyword = cmd_list[2].strip()
            if keyword.startswith('"') and keyword.endswith('"'):
                keyword = keyword[1:-1]
                tmp_result = []
                if cmd_list[1] == "title":
                    tmp_result = self.central_store.search_by_title(keyword)
                elif cmd_list[1] == "artist":
                    tmp_result = self.central_store.search_by_artist(keyword)
                else:
                    print "Wrong option " + cmd_list[1] + '.'
                for t in tmp_result:
                    print t
            else:
                print "Wrong keyword" + cmd_list[2] + '.'

        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'


    def song(self, cmd_line):
        cmd_list = cmd_line.split()

        if cmd_list[0] == "song" and len(cmd_list) == 2:
            try:
                print self.central_store.song_dic[int(cmd_list[1])]
            except ValueError, e:
                print "Wrong songId " + cmd_list[1] + "."
            except KeyError, e:
                print "Song " + cmd_list[1] + " doest not exist."
        else:
            print "Wrong command " + cmd_line + '.'


    def sort(self, cmd_list):
        if len(cmd_list) == 2:
            if cmd_list[1] == "title":
                self.central_store.sort_by_title(self.central_store.song_list)
                self.central_store.print_song_list(self.central_store.song_list)
            elif cmd_list[1] == "artist":
                self.central_store.sort_by_artist(self.central_store.song_list)
                self.central_store.print_song_list(self.central_store.song_list)
            #elif cmd_list[1] == "songId":
            else:
                print "Wrong option " + cmd_list[1]
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'


    def delete(self, cmd_list):
        if len(cmd_list) == 2:
            try:
                song = self.central_store.song_dic[int(cmd_list[1])]
                if song in self.central_store.playlists[self.curr_playlistId][1]:
                    self.central_store.playlists[self.curr_playlistId][1].remove(song)
                    #Do not need to care about indices of python list
                else:
                    print "Song " + str(song.songId) + " does not exist in the current playlist."
            except ValueError, e:
                print "Wrong songId " + cmd_list[1] + "."
            except KeyError, e:
                print "Song " + cmd_list[1] + " doest not exist."
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'


    def insert(self, cmd_list):
        if len(cmd_list) == 2:
            try:
                song = self.central_store.song_dic[int(cmd_list[1])]
                if song in self.central_store.playlists[self.curr_playlistId][1]:
                    print "Song " + str(song.songId) + " already exists in the current playlist."
                else:
                    self.central_store.playlists[self.curr_playlistId][1].append(song)
            except ValueError, e:
                print "Wrong songId " + cmd_list[1] + "."
            except KeyError, e:
                print "Song " + cmd_list[1] + " doest not exist."
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'


    def insert_search(self, cmd_list):
        if len(cmd_list) == 3:
            keyword = cmd_list[2].strip()
            if keyword.startswith('"') and keyword.endswith('"'):
                keyword = keyword[1:-1]
                tmp_result = []
                if cmd_list[1] == "title":
                    tmp_result = self.central_store.search_by_title(keyword)
                elif cmd_list[1] == "artist":
                    tmp_result = self.central_store.search_by_artist(keyword)
                else:
                    print "Wrong option " + cmd_list[1] + '.'

                for t in tmp_result:
                    self.insert(["insert", str(t.songId)])
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'

    def main(self, cmd_line):
        cmd_list = cmd_line.split()

        if cmd_list[0] == "main" and len(cmd_list) == 1:
            self.curr_menu = "main"
            self.curr_playlistId = None
        else:
            print "Wrong command " + cmd_line + '.'


    def print_curr_playlist(self, cmd_list):
        if len(cmd_list) == 1:
            self.central_store.print_playlist(self.curr_playlistId)
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'


    def search_playlist(self, cmd_list):
        if len(cmd_list) == 3:
            keyword = cmd_list[2].strip()
            if keyword.startswith('"') and keyword.endswith('"'):
                keyword = keyword[1:-1]
                tmp_result = []
                if cmd_list[1] == "title":
                    tmp_result = self.central_store.search_by_title(keyword,
                                                                    self.central_store.playlists[self.curr_playlistId][1])
                elif cmd_list[1] == "artist":
                    tmp_result = self.central_store.search_by_artist(keyword,
                                                                    self.central_store.playlists[self.curr_playlistId][1])
                else:
                    print "Wrong option " + cmd_list[1] + '.'

                self.central_store.print_song_list(tmp_result)
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'

    def sort_playlist(self, cmd_list):
        if len(cmd_list) == 2:
            if cmd_list[1] == "title":
                self.central_store.sort_by_title(self.central_store.playlists[self.curr_playlistId][1])
                self.print_curr_playlist(["print"])
            elif cmd_list[1] == "artist":
                self.central_store.sort_by_artist(self.central_store.playlists[self.curr_playlistId][1])
                self.print_curr_playlist(["print"])
            #elif cmd_list[1] == "songId":
            else:
                print "Wrong option " + cmd_list[1]
        else:
            print "Wrong command " + ' '.join(cmd_list) + '.'