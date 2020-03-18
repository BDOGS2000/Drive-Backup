import os
from os import listdir, unlink
from os.path import isfile, join

copy_drive_path = "G:\\My Drive\\d_backup"


def lol():
    onlyfiles = [f for f in listdir(copy_drive_path) if isfile(join(copy_drive_path, f))]
    for i in onlyfiles:
        if i.split(".")[1] == "zip":
            print("got it")


if __name__ == "__main__":
    lol()
