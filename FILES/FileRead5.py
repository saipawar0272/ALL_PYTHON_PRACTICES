try:
    filename=input("Enter any file name:")
    with open(filename,"rt") as si:
        filedata=si.read()
        print("*"*50)
        print(filedata)
except FileNotFoundError:
    print("file not exist")
except OSError:
    print("os not giving prmission")