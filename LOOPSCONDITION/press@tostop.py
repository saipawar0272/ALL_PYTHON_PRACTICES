#program for reading list of values  from keyboard and display those values

import sys
print("enter number of values and press @ to stop:")
lst=[]
while("KVR"):
    value=input()
    if(value=="@"):
        if(len(lst)==0):
            print("list is empty")
        else:
            print("content of lst",lst)
        sys.exit()
    else:
        lst.append(float(value))


