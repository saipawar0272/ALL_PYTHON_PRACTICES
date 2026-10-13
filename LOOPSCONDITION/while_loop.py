# wap which will genrate one to n numbers  where n must be the positive integer,

n=int(input("enter number:"))

if(n<=0):
    print("invalid/negative/zero nimber",n)
else:
    print("numbers with in: {}".format(n))

    i=1 #initialization
    while(i<=n):  #condition
          print("\t{}".format(i))
          i=i+1 # updation part

