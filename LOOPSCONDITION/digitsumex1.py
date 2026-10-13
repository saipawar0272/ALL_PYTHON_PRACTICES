#program for finding  sum of digits of given number
#given input
#expected output : 22(3+4+7+8)
num=int(input("Enter a number:"))
sum=0
tn=num
while(num>0):
    d=num%10
    sum=sum+d
    num=num//10
else:
    print("sum of digits of {}={}".format(tn,sum))







