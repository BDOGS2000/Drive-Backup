import requests
import os
import shutil
import datetime

main_drive = "D"
copy_drive = "G"


def clone_drive():
    g_drive_name = copy_drive + ":\\My Drive\\d_backup\\BU"
    shutil.make_archive(g_drive_name, 'zip', 'D:\\school')
    print("done")


def find_drive():
    if os.system("vol %s: 2>nul>nul" % main_drive) == 0 and os.system("vol %s: 2>nul>nul" % copy_drive) == 0:
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


if __name__ == "__main__":
    if connected():
        clone_drive()
    else:
        print("yeeeeet")
