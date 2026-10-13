#program which will demonstrate opening the file and properties of file.

try:
     kvr=open("kvr.data","r")
     print("file fetched Successfully")
except FileNotFoundError:
     print("file not exist")
else:
     print("File opened in read mode successfully")
     print("type of kvr=",type(kvr))
finally:
     print("i am from finally block")
     print("is file closed=",kvr.closed)
     kvr.close() #close file manually
     print("is file closed=",kvr.closed)