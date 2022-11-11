import os
import sys

folder_exists = folder_created= 0

while True:

    name_stt = int(input("start: "))
    name_end = int(input("end: "))

    for i in range(name_stt, name_end+1):
        if (os.path.exists(str(i)) and os.path.isdir(str(i))):
            print("folder already exists: " + str(i))
            folder_exists = folder_exists + 1
        else:
            os.mkdir(str(i))
            print("folder created: " + str(i))
            folder_created = folder_created + 1

    print("Created:", folder_created, "Exists:", folder_exists, "Total:", folder_created+folder_exists)
    
    stop = input("continue? (Y/N) ")   

    if 'y' in stop or 'Y' in stop:
        continue
    else:
        sys.exit()