#program for  remove file name
import os
try:
    os.remove("hyd.info")
    print("file removed")
except FileNotFoundError:
    print("file not exist")
