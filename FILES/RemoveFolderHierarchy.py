#python program which will remove folder heirarachy
import os
try:
    os.removedirs("C:\\oracle") #past the folder path
    print("folder removed")
except FileNotFoundError:
    print("file not available")
except OSError:
    print("file is not empty")

