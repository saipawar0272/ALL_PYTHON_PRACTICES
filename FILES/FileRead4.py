#program for displaying the content of any file name

try:
    filename=input("Enter Any file Name:")
    with open(filename,"rt") as si:
        filedata=si.readlines()
        print("*"*50)
        for line in filedata:
            print(line,end="")
        print()
except FileNotFoundError:
    print("file not exist")