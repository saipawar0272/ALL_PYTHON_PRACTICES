#wap accept dynamic no pf values in list nd print the list elements .accept elements from keyboard and search in list
#if the elements is found then display its position.otherwise the display element does not exists

n=int(input("enter number:"))
if(n<=0):
    print("invalid number:")
else:
    lst=list()
    for i in range(1,n+1):
        print("enter valyes {}".format(i))
        val=int(input())
        lst.append(val)
    else:
        print("elements of list:")
        for val in lst:
            print("{}\n".format(val),end="")
            print("enter which element you want to search:")
            selement=int(input())
            res=False
            for i in range(0,len(lst)):
                if(lst[i]==selement):
                    res=True
                    break
            if(res):
                        print("element is found successfully",i)
            else:
                        print("element does not exists")