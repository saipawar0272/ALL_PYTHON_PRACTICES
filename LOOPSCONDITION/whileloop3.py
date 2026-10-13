#wap program which will genrate multiplication table give number including positive and negative

n=int(input("enter number:"))
if(n==0):
    print("zero is not valid",n)
else:
    print("multiplication table for {}",n)
    i=1
    while(i<11):
        print("\t{}*{}={}".format(i,n,i*n))
        i=i+1

