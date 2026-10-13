#wap program to grenrate multiplication table

n=int(input("enter number:"))
if(n<=0):
    print("invalid number:{}",n)
else:
    print("numbers within {}",n)
    i=1  #initialize
    while(i<=10): #condition
        print("\t{}*{}={}".format(i,n,i*n))
        i=i+1 #update
