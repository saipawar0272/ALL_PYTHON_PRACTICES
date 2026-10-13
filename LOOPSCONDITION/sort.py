lst=[]
n=int(input("enter number of elements:"))
for i in range(n):
     lst.append(float(input("enter number:")))

     lst.sort()
     print("elements in ascending order \n{}".format(lst))

     lst.reverse()
     print("elements in descending order \n{}".format(lst))

