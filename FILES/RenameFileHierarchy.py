#program for renaming file

import os
try:
    os.rename("json1.py","json6.py")
    print("file name renamed")
except FileNotFoundError:
    print("file not exist")