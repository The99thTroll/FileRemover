import time
import os
import shutil

path = "/Users/albrino/Desktop/WhitehatJr_Stuff/P99/junk"
day = time.time();
dateToDelete = 30
files = None
filePaths = []

if os.path.exists(path):
    for dirPath, subdir, files in os.walk(path):
        for x in files:
            filePaths.append(os.path.join(dirPath, x))
    for y in filePaths:
        if os.stat(y).st_ctime+(86400*dateToDelete) < day:
            print("Deleting...")
            if os.path.isfile(y):
                os.remove(y)
            else:
                shutil.rmtree(y)
        else:
            print("File not marked for deletion")

else:
    print("Path not found")