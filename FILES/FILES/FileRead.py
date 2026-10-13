#program to demonstrate reading the data from keyboard

try:
    with open("hyd.info") as si:
        fildata=si.read()
        print(type(fildata))
        print(fildata)
except FileNotFoundError:
    print("file does not exist")
