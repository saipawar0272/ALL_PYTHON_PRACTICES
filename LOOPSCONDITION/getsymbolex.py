#program for only special characters
line=input("enter test:")
nosp=0
print("given line=",line)
for ch in line:
    if(not ch.isalnum()):
        nosp=nosp+1
        print("{}".format(ch))
    else:
        print("number of Special symbols= {}",nosp)