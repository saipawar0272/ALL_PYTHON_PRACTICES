#program to demonstrate random access file

with open("hyd.info","r") as si:
    print("*"*50)
    print("initial index of si=",si.tell())
    filedata=si.read(5)
    print("file data=",filedata)
    print("now index of si=",si.tell())

    #reset si at 10th index

    si.seek(10)
    filedata=si.read(6)
    print("file data=",filedata)
    print("now index of si=",si.tell())
    print("*"*50)
