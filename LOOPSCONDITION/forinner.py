for i in range(1,6):
    print("val of i-outer loop={}".format(i))
    for j in range(1,4):
        print("val of j-inner loop={}".format(j))
    else:
        print("\tOut-off inner loop")
else:
    print("\tOut-off outer loop")