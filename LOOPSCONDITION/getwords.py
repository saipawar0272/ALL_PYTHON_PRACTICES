#program to find out words from data
line=input("enter text:")
nosp=0
print("given line=",line)
words=line.split()
for word in words:
  for ch in word:
    if((not ch.isalnum()) and (not ch.isspace()) ):
        nosp=nosp+1
        print("{}".format(ch))
    else:
        print("number of special symbols=",nosp)