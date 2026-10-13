#type of int float bool string
#int to float

lst1=[45,63,49,19,[45,69,78,23]]
print(lst1,type(lst1))

lst2=( (45,67,34,74,77),56,96,23,78)
print(lst2,type(lst2))

lst3={'a':23,'b':63,'c':85,"d":{'a':96,'b':63},'e':639}
print(lst3)

a=lst1[3]
print(a)

b=lst3.values()
print(b)
d=lst3.keys()
print(d)

b=(lst3["b"])
print(b)

print(len(lst1))
print(len(lst2))
print(len(lst3))

s1=['sai','ram','shyam']
print(s1)
print(s1[1:2])

s=[56,89,26,516,896,446,896,6926,964,45,4852]

print(s[1:6:2])

s='python'
rev=s[::-1]
print(rev)

lst=[56,39,29,29,29,46,49,264,656,26]
rev=lst[::-1]
print(rev)

lst.reverse()
print(lst)

s.split()
print(s)

a=lst.count(29)
print(a)

lst2=[56,89,26,51,64,656,16,32,41]

lst3=lst2+lst
print(lst3)

tup1=(89,45,52,6,3,8,6,6,56,56,74)
tup2=(89,23,45,2,4,1,645,6)
tup3=tup1+tup2
print(tup3)

set1={56,96,6,23,46}
set2={89,715,6,26,45}

set3=set1|set2
print(set3)
set4=set1^set2
print(set4)

d1={"a":20,'b':36,'c':89,'d':74}
d2={'e':56,'f':69,'g':78,'h':52}
d3=d1|d2
print(d3)

d1=[56,89,45,12,35,459,8]
print(d1,type(d1))

d1.sort()
print(d1)

s='python_lang'

print(s,type(s))

s='python_prog'
print(s,type(s))

print(s[1:6:2])

print(d1[1:5:2])

print(s[::-1])

d1.reverse()
print(d1)

d1.append(56)
d1.append(89)
d1.append(56)
d1.append(56)
d1.append(89)
d1.append(56)
print(d1)

d1.