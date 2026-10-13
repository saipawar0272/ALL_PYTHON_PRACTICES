#python program which will accept from list of words whose length is 2 or 4
print("enter list of words seprated by comma:")
word24=[str(word) for word in input().split() if len(word) in [2,3,4]]
print("words with 2 or 4 in length=",word24)
