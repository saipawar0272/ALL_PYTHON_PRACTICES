#program which will rename folder
import os
try:
    os.rename("HYD","java")
    print("file renamed successfully")
except FileNotFoundError:
    print("file not exist")