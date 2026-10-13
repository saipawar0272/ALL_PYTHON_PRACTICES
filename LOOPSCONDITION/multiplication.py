#wap program which will display mul table for various selected values

nom=int(input("enter number:"))
if(nom<=0):
    print("invalid number")
else:
    lst=list()
    for n in range(1,nom+1):
        print("enter number for which you want table:")
        v=int(input())
        lst.append(v)
    else:
        print("mul table you want",lst)
    for n in lst:
        print("\t mul table for :{}".format(n))
        for i in range(1,11):
            print("\t {}*{}={}".format(i,n,i*n))
        else:
            print("-"*20)
    else:
        print("all mul table are printed above")

