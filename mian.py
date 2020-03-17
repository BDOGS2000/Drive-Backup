import requests
import os
import shutil

main_drive = "D"
copy_drive = "G"


def find_drive():
    if os.system("vol %s: 2>nul>nul" % main_drive) == 0 and os.system("vol %s: 2>nul>nul" % copy_drive) == 0:
        space()
    else:
        return False
            

def internet_check():
    return requests.get('https://google.com').ok


def connected():
    if find_drive() and internet_check():
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
    print(connected())
