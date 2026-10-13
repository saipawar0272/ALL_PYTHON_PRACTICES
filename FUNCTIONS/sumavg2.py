#python program which will accept list of words and highest length words
def getwords():
    print("enter list of words and press @ to stop:")
    lst=[]
    while(True):
        val=input()
        if(val=="@"):
            break
        else:
            lst.append(val)
    return lst

def findmaxlenword(words):
     if(len(words)==0):
         print("List is empty--can't find max length word")
     else:
        d=dict()
        for word in words:
             d[word]=len(word)
        else:
            lst=[]
            print(d)
            ml=max(list(d.values())) #ml=8
            for word,length in d.items():
                if(length==ml):
                    lst.append(word)
            else:
                     print("max len words")
                     for word in lst:
                         print("\t{}".format(word))
                     else:
                         print("number of max length words=",len(lst))




#main program
words=getwords()
findmaxlenword(words)
