#program to obtain special symbol and their count without spaces
from curses.ascii import isalpha

line=input("enter line of text:")
nosp=0
print("given line=",line)
for ch in line:
    if((not ch.isalnum()) and  (not ch.isspace()) ):
        nosp=nosp+1
        print("{}".format(ch))
    else:
        print("number of special symbols=",nosp)