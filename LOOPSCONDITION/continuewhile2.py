#write python program which will accept  lis of words from keyboard and display thise words whose length either 3 or 5.
nov=int(input("how many words you want to enter:"))
if(nov<=0):
    print("{} is invalid input".format(nov))
else:
    lst=[]
    for i in range(1,nov+1):
        val=input("enter {} value:".format(i))
        lst.append(val)
    else:
        print("list of words={}".format(lst))
        #code for obtaining those words whose length in either 3 or 5
        word35=list() #for storing 3 or 5 length word
        for word in lst:
            if(len(word) not in [3,5]):
                continue
            word35.append(word)
        else:
            print("list of words with 3 or 5 in length")
            print(word35)


