import requests
import os
import shutil

main_drive_letter = "D"
copy_drive_letter = "G"


def find_drive(main, copy):
    if os.system("vol %s: 2>nul>nul" % main) == 0 and os.system("vol %s: 2>nul>nul" % copy) == 0:
        space()
    else:
        return False
            

def internet_check():
    return requests.get('https://google.com').ok


def connected():
    if find_drive(main_drive_letter, copy_drive_letter) and internet_check():
        return True
    else:
        return False


def space():
    usage_main = list(shutil.disk_usage(main_drive_letter + ":"))
    usage_copy = list(shutil.disk_usage(copy_drive_letter + ":"))
    if usage_main[1] <= usage_copy:
        return True
    else:
        return False


if __name__ == "__main__":
    print(connected())
