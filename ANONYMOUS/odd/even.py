#wap program which will filter out the elements even odd

lst=[45,89,26,57,56,5,69,6,896,26,47,41,52,58,636,36,77,55,99,33]

p1=tuple(filter(lambda x:x%2==0,lst))

print("original numbers={}",lst)
print("even numbers ={}".format(p1))

n1=tuple(filter(lambda c:c%2!=0,lst))
print("odd numbers={}".format(n1))
