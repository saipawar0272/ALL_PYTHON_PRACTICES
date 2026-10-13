#program for listing the file in folder

import os
try:
    foldername=input("enter folder name for listing file:")
    FilesLists=os.listdir(foldername)
    print("List of Files")
    print("Number of Files=",len(FilesLists))
    print("*"*50)
    for filename in FilesLists:
        print(filename)
except FileNotFoundError:
    print("file not exist")

