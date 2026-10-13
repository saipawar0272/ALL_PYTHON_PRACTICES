nom=int(input("enter number:"))
if(nom<=0):
    print("invalid number")
else:
    for n in range(1,nom+1):
        print("mul table for :{}".format(n))
        for i in range(1,11):
            print("\t{}*{}={}".format(n,i,n*i))
        else:
            print("*"*20)
    else:
        print("all mul table are printed above")
