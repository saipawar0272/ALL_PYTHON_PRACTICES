with open("kvr.data","r") as kvr:
    print("*"*50)
    print("File Opened in read mode Successfully")
    print("type of KVR=",type(kvr))
    print("*"*50)
    print("Is file closed within 'With open() as'=",kvr.closed)
    print("\n")
    print("Is file closed after 'with open() as' Indentation=",kvr.closed)