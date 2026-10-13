#write python progra which will accept only palindrome word
print("enter number of words and press any special symbol to stop:")
lst=[]
while(True):
    value=input()
    if(not value.isalnum()):
        break
    else:
        lst.append(value)
        print("list of words=",lst)
        #code for obtaining palindrome words
        plist=list() #for storing palindrome words
        for word in lst:
            if(word!=word[::-1]):
                continue
                plist.append(word)
            else:
                print("list of palindrome words")
                print(plist)