for i in range(6,0,-1):
    print(" val of i-outer loop{}".format(i))
    j=1
    while(j<=3):
        print("\t val of j-inner loop={}".format(j))
        j=j+1
    else:
        print("\tOut-off inner loop")
else:
    print("\t out-off outer loop")
