with open("kvr.data", "w") as kvr:
    print("File created and opened in write mode")
    print("file name:",kvr.name)
    print("file name:",kvr.mode)
    print("Is file Readable=",kvr.readable())
    print("is file writable=",kvr.writable())
    print("is file closed=",kvr.closed)