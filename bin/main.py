import sys
sys.path.append("..")


from bin.con.song import CentralStore
from bin.ctrl.rw import load_song_list, load_menu

from bin.ui.repl import REPL


if __name__ == "__main__":
    tmp_song_list = load_song_list()

    tmp_menu = load_menu()

    rEPL = REPL(CentralStore(tmp_song_list), tmp_menu)

    while True:
        rEPL.repl()

