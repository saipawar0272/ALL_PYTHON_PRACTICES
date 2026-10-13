#program which will list the file present in folder

import os

FilesList=os.listdir(".") #here (".") represent to current working folder directory

for Files in FilesList:
    print("list of file\n",Files)
    print("number of files",len(Files))
