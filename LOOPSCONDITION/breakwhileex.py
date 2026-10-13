#program for breaking statement using while and break
s="PYTHON"
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("i am from else part of the loop")
    print("______________________")
    #my rwquirement is to display "pyt" without using indexing and slicing
    i=0
    while(i<len(s)):
        if(s[i]=="H"):
            break
            print(s[i],end="")
            i=i+1
    
        
