import requests
import os
import shutil
from datetime import datetime
from os import listdir, unlink
from os.path import isfile, join
import time
from tqdm import tqdm
import multiprocessing


main_drive = "D"
copy_drive = "G"
copy_drive_path = copy_drive + ":\\My Drive\\d_backup"


def exist_check():
    only_files = [f for f in listdir(copy_drive_path) if isfile(join(copy_drive_path, f))]
    for i in only_files:
        if i.split(".")[1] == "zip":
            unlink(copy_drive_path + "\\" + i)


def clone_drive():
    shutil.make_archive(copy_drive_path + "\\BU_" + str(datetime.date(datetime.now())), 'zip', main_drive + ':\\everything')


def find_drive():
    if os.system("vol %s: 2>nul>nul" % main_drive) == 0 and os.system("vol %s: 2>nul>nul" % copy_drive) == 0:
        exist_check()
        if space():
            return True
        else:
            return False
    else:
        return False


def internet_check():
    return requests.get('https://google.com').ok


def connected():
    if internet_check() and find_drive():
        return True
    else:
        return False


def space():
    usage_main = list(shutil.disk_usage(main_drive + ":"))
    usage_copy = list(shutil.disk_usage(copy_drive + ":"))
    if usage_main[1] <= usage_copy[2]:
        return True
    else:
        return False


def loading():
    while p.is_alive():
        for _ in tqdm(range(100)):
            time.sleep(0.1)


if __name__ == "__main__":
    if connected():
        exist_check()
        p = multiprocessing.Process(target=clone_drive)
        p.start()
        loading()
        p.join()
        print("Done!!!!")
    else:
        print("error")
