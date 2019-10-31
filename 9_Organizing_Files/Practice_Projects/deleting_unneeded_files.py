import os

for foldername, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if os.path.getsize(os.path.abspath(filename)) > 2**20:
            print(os.path.abspath(filename))
