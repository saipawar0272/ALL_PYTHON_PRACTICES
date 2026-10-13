#program for finding sum of digits of given number using for loop
#give input : 5866
#expected output:25
num=input("enter number:")
sum=0
for d in num:
    sum=sum+int(d)
else:
    print("sum of digits of {}={}".format(num,sum))