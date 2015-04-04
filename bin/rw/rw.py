from bin.con.song import SongFile


def load_song_list(filename):
    file = open("../../data/" + filename, "rt")

    tmp_song_list = []
    tmp_songId = -1
    for line in file:
        tmp_songId += 1
        tmp_list = line.split(",")
        tmp_song_list.append(SongFile(tmp_songId, tmp_list[0].strip(), tmp_list[1].strip()))

    return tmp_song_list


if __name__ == "__main__":
    load_song_list("SongList.txt")