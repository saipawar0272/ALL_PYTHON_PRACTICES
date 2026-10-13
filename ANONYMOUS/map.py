#wap program which accept list of integer values and square them

def square(x):
    return x**2

print("enter integer values dynamically seprted with space")
oldlst=[int(x) for x in input().split()]

sqlist=list(map(square,oldlst))
print("*"*20)

print("old list={}".format(oldlst))
print("new list-{}".format(sqlist))