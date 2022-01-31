import os
import shutil

"""
The content gets copied from folder1 to folder2 in the same directory as this file
"""
for foldername, subfolders, filenames in os.walk(os.path.abspath('folder1')):
    for filename in filenames:
        if filename.endswith('.pdf') or filename.endswith('.jpg'):
            print("Copying", filename)
            newPath = os.path.join(os.path.abspath(
                'folder2'), os.path.relpath(foldername, 'folder1'))
            if not os.path.exists(newPath):
                os.mkdir(newPath)
            shutil.copy(os.path.join(foldername, filename), newPath)
