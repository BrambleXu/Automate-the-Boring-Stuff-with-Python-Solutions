import os
import re

# Change these to whatever you want
prefix = "spam"
foldername = "test"

for _, _, filenames in os.walk(foldername):
    for filename in filenames:
        mo = re.match(prefix + r'(\d+)\.txt', filename)
        if mo:
            print(mo.group(1))
            print(int(mo.group(1)))
