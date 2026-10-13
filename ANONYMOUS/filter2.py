#main program

lst=[10,20,-45,-89,-23,-44,303,0,-465,78,45]
p1=tuple(filter(lambda x:x>0,lst))
print("*"*10)

print("original value of list={}",lst)
print("positive value of list={}".format(p1))
n1=tuple(filter(lambda a:a<0,lst))
print("negative values of list={}".format(n1))