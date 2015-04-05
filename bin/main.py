from bin.con.song import CentralStore
from bin.ctrl.rw import load_song_list

from bin.ui.repl import REPL


if __name__ == "__main__":
    tmp_song_list = load_song_list("SongList.txt")

    rEPL = REPL(CentralStore(tmp_song_list))

    while True:
        rEPL.repl()

