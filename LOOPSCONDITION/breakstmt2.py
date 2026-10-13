#program for demonstrating break keyword
s="MISSISSIPPI"
print("by using for loop")
for ch in s:
    print("\{}".format(ch))
else:
    print("i am from else part of for loop")
    print("_____________")
    #my requirement is to display miss without u=indexing and slicing
    ni=0
    i=0
    while(i<len(s)):
        if(s[i]=="I"):
            ni=ni+1
            if(ni==2):
                break
                print(s[i],end="")
                i=i+1
            else:
                print("i am from else part of for loop")
                print("\n other statements in program")
