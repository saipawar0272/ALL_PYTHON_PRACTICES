try:
    with open(hyd.info) as si:
        filedata=si.readlines()
        for line in filedata:
            print(line,end="")
except FileNotFoundError:
    print("file not exist")