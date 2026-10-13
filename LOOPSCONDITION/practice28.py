a=12.32
b=20
c=a+b
print(c)
print(type(c),c)

a=0b1011010
print(a)

b=0x123746
print(b)
c=0x11
print(c)

a1=bin(10)
print(a1)
b1=bin(46)
print(b1)

c1=oct(255)
print(c1)

c2=oct(44998446)
print(c2)

c3=oct(7998989)
print(c3)

c4=hex(8986568665)
print(c4)

c5=hex(48798583565)
print(c5)

c6=hex(65985689898)
print(c6)

a=float(34)
print(a)
b=float(89)
print(b)

c=bool(45464)
print(c)
c=bool(0)
print(c)
d=complex(4+5j)
print(d)
e=complex(6+9j)
print(e)
f=complex(8+5j)
print(f)
a=10
print(type(a))
print(str(a))
print(a)
print(type(a))
a=str(10)
print(a,type(a))
print(str(12.35))

c=34
print(str(c))
c=str(56)
print(c,type(c))

s1='rossum'
print(s1,type(s1))

print(s1[2])
print(s1[2:5])
print(s1[:])
print(s1[:6])
print(s1[:48])
print(s1[2:8])
print(s1[2:])
print(s1[-7:2])
print(s1[-5:-2])

print(s1[-6:-2])
print(s1[0:4])
l=[45,65,12]
b=bytes(l)
print(b)

d=(5,89,255)
e=bytes(d)
print(e)

e={56,89,46}
f=bytes(e)
print(f,type(f))

r=range(6)
print(r,type(r))


for x in range(10,21):
    print(x)

for x in range(45,56):
    print(x,type(x))

for x in range(5,55,5):
    print(x)

for x in range(2,22,2):
    print(x)

l1=[10,23,56,89,26,26,56]
print(l1,type(l1))

print(l1[2])

print(l1[2:4])

l1.append('sai')
print(l1)

##l1.sort(key=int)
##print(l1)

l1.insert(2,89999)
print(l1)
l1.insert(6,'ramesh')
l1.insert(85,'rakshs')
print(l1)

l1.pop()
print(l1)
l1.pop(2)
print(l1)

l1.remove(23)
print(l1,type(l1))

l1.index('ramesh')
l1.index(56)
print(l1)

l1.remove(56)
print(l1)

##l1.remove(996) -- error-x not in list

l2=l1.copy()
print(l2,l1)
print(l1+l1)
print(id(l1),id(l2))

print(l1)
print(l2)
l2=l1
print(l1,l2)
print(id(l1),id(l2))
l1.append("AI")
print(l1,l2)

l1.reverse()
print(l1)

c1=['sai','ganesh','ram','shyam']
print(c1)
c1.sort()
print(c1)

c1.clear()
print(c1,type(c1))

l1.extend(c1)
print(l1)

c1={2:'soma',4:'00000'}  #key_value object is not supported in list --it gets only keys in the extend
print(c1)

l1.extend(c1)
print(l1)

l1.count(10)
print(l1)


a1=[10,'sai',['c','python','java'],[56,89,78]]
print(a1)

print(a1[2])
print(a1[2][-3:1])
print(a1[-3:-1])
print(a1[2][-3:1])



c=(45,'sai',856,['ganesh','ramesh','ganga','nanaga'])
print(c,type(c))

print(c[3][-4:-1])


s={10,'hyd'}
s.add('india')

print(s,type(s))

s.clear()
print(s,type(s))


s1={10,20,30,'sai','ram'}
s2={45,52,10,20,'ganesh','soma'}

print(s1,type(s1))
print(s2,type(s2))

s1.pop()
print(s1)
s1.add('ram')
print(s1)
print(s1)
print(s1)
s1.add('sai')

c1=(45,98,'sai',(45,56,78,'soma'),'ram')
print(c1,type(c1))

print(c1[3])
print(c1[3][3])
print(c1[-2][-4])

c2= s1.issubset(s2)
print(c2)

c3=s2.issubset(s1)
print(c3)

c1=s1.isdisjoint(s2)
print(c1)
c2=s2.isdisjoint(s1)
print(c2)

c2=s1.union(s2)
print(c2)
c2=s1.intersection(s2)
print(c2)
c2=s2.intersection(s1)
print(c2)

print(s1|s2)
print(s1 & s2)
print(s1-s2)
print(s2-s1)
#print(s1+s2)  #error-unsupported operand type

##print(s1%s2)

s3=s1.symmetric_difference(s2)
print(s3)


s3=s1.symmetric_difference_update(s2)
print(s3)
print(s1)

s1.update(s2)
print(s1)

s2=s1.copy()
print(s2)

s1=s2.copy()
print(s1)

d1={}
print(d1,type(d1))

d1={1,2,3}
e1={1:'sa',
    2:'ramesh'}

print(d1,type(d1))
print(e1,type(e1))


s1={1:'sai',2:'ramesh',3:'soma',4:'golya'}
print(s1)
s2={1:'vushal',2:'shavkar',3:'rahul'}
print(s2)

c1=s1.get(3)
print(s1)
print(c1)
c1=s1.values()
print(c1)

c1=s1.keys()
print(c1)

##s1.pop('')

print(s1)
print(s2)

s1.update(s2)
print(s1)
print(s2)
c1=s1.update(s2)
print(c1)





