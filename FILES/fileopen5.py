#
try:
    with open("kvr.data", "x") as kvr:
         print("file created in read mode")
         print("file name=",kvr.name)
         print("file mode",kvr.mode)
         print("is readable",kvr.readable())
         print("is writable",kvr.writable())
         print("is closed",kvr.closed)
except FileNotFoundError:
    print("file not exist")