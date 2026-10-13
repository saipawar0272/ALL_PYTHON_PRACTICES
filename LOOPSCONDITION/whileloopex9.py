#python program to generate square  of positive integer
n=int(input("enter the number:"))
i=1#initialization
while(i<=n):
    print("multiplication table of ({}*{})={}".format(n,i,n*i))
    i=i*n