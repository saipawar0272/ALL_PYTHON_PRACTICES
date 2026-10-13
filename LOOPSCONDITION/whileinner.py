i=1
while(i<=6):
    print(" val of i-outer loop{}".format(i))
    j=1
    while(j<=3):
        print("\t val of j-inner loop={}".format(j))
        j=j+1
    else:
        print("\t out-off inner loop")
        i=i+1
else:
    print("Out-off outer loop")