#python program for accept list of numerical values and display multiplication table for those random numbers
n=int(input("enter number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=list()
    for i in range(1,n+1):
        val=int(input("enter {} val for generating mul table".format(i)))
        lst.append(val)
    else:
        print("given list og values:{}".format(lst))
        #code for mul table for random numbers
        for num in lst: #outer for loop supply the number from list
            if(num<=0):
                print("{} is invalid input".format(num))
            else:
                print("-------------------------------")
                print("mul table for:{}".format(num))
                print("--------------------------------")
                for i in range(1,11):
                    print("{}*{}={}".format(i,n,num*i))
                else:
                    print("------------------------------")