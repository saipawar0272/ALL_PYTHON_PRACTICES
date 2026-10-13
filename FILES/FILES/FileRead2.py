#program for displaying the content of any file name:
try:
    filename=input("Enter any file name here:")
    with open(filename,"rt") as si:
        filedata=si.read()
        print(filedata)
except FileNotFoundError:
     print("file does not exist")