#program which will accept list of employee salaries and obtain those salaries which are come in between 0 to 500 and give 10% hike and 20% hike to those who range in between 500 to 2k
 #print total salary of 10% hiked employees ans 20%hiked employees
 #maxsal=1000 && minsal=0

print("enter salaries sperated by space:")
sals=[float(sal) for sal in input().split(",") if 0<=float(sal)<1000]
#obtain salaries ranges from 0 to 501
sal0_500=list(filter(lambda sal: 0<=sal<=500,sals))
sal500_1000=list(filter(lambda sal: 501<=sal<=1000,sals))
print("sal<500={}".format(sal0_500))
print("sal<1000={}".format(sal500_1000))

#give 10% hike to those whose sal in between 0 to 500

hksal0_500=list(map(lambda sal:sal+sal*10/100,sal0_500))
hksal500_1000=list(map(lambda sal:sal+sal*10/100,sal500_1000))

print("*"*50)
print("sal0_500\t\thiked sal 0_500")
print("="*50)
for osl,nsl in zip(sal0_500,hksal0_500):
    print("\t{}\t\t{}".format(osl,nsl))
    print("*"*50)
    print("+"*50)

print("sal500_1000\t\thiked sal500_1000")
print("="*50)
for osl,nsl in zip(sal500_1000,hksal500_1000):
    print("\t{}\t\t{}".format(osl,nsl))
    print("*"*50)