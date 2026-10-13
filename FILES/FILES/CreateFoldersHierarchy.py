#program for creating folders key
import os
try:
    os.makedirs("C:\\INDIA\\MH\\MUM\\NIT\\PYTHON")
    print("Folder hiearchy created")
except FileExistsError:
    print("file already created")
