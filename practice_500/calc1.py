import calc

print("addition of two number",calc.add(5,9))
print("substraction of two numbers",calc.substract(9,6))
print("multiplication of two numbers",calc.multiply(9,6))
print("division of two numbers",calc.division(45,4))


l1=[56,89,26,56]
print(l1)
l1.append(123)
print(l1)
l1.insert(0,123)
print(l1)
l1.reverse()
print(l1)
l1.append([56,89,23])
print(l1)
# print(l1[5[0]])
l1.index(89,1)
print(l1)

print(l1[6:1])
print(l1)

l2=l1[6:1]
print(l2)



l1=[55,56,456,359,[89,56]]
print(l1[4][1])


v=[2,3,4]
s=-3
d=print(v*s)
print(d)

x=[]
for i in v:
    x.append(i*s)
    print(x)

l=[1,2,3,4,5]

s=[]
for i in l:
    s.append(i**2)
    print(s)

s=[i**2 for i in l]
print(l)