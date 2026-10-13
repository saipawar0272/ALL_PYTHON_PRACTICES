#python program which will accept line of text and find length of each word
line=input("line of texts:")
print("given line",line)
words=line.split()
print("---------------------------------")
for word in words:
     print("{}--->{}".format(word,len(word)))
     print("----------------OR-----------------")
     wl=dict()
     for word in words:
         wl[word]=len(word)
     else:
         for k,v in wl.items():
             print("\t{}---->{}".format(k,v))





     wt=list()
     for word in words:
        wt.append((word,len(word)))
     else:
        print(wt)
