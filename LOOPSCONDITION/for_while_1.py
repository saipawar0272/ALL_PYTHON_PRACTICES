tpl=(10,'kvr','oucet',12.34,'nit','true')
print("elements in list:")
for val in tpl:
    print(val)
else:
    print("*"*30)

s={45,'sai','ram','shyam',96,79,26}
print("elements in list")
for val in s:
    print(val)
else:
    print("*"*30)

d={1:'sai',2:'ram',3:89,4:'ganesh',5:96}
print("key/value")
for k,v in d.items():
    print("\t{}\t{}".format(k,v))
else:
    print("*"*30)
