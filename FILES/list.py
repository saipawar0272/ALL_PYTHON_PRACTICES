#program which will list the file present in folder

import os

FilesList=os.listdir("C:\\Users\\saipr\\PycharmProjects\\FILES")

for File in FilesList:
    print("list of file\n",File)
    print("number of files",len(File))
