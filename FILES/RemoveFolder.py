#program which will remove folder

import os
try:
    os.rmdir("C:\\oracle")
    print("Folder Removed")
except FileNotFoundError:
    print("file not available")
except OSError:
    print("the file is not empty")