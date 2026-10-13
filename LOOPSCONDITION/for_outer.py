#wap which will generate multiplication table where n must be the positive interger

n=int(input("enter number:"))
if(n<=0):
    print("invalid number",n)
else:
    print("multilplication table for {}".format(n))
    i=1

    for i in range(1,11):
        print("{}*{}={}".format(i,n,i*n))
