import requests
import platform
import os
import shutil

main_drive_letter = "D"
copy_drive_letter = "G"


def hasdrive(main, copy):
    if os.system("vol %s: 2>nul>nul" % (main)) == 0 and os.system("vol %s: 2>nul>nul" % (copy)) == 0:
        return True
            

def internet():
    return requests.get('https://google.com').ok

def connected():
    if hasdrive(main_drive_letter, copy_drive_letter) and internet():
        status = True
    else:
        status = False
    return status

def space():
    total, used, free = shutil.disk_usage("/")



if __name__ == "__main__":
    if connected():
        """meh"""