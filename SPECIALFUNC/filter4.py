#program which will accept list of numerical values and obtain positive even numbers

print("enter list of values:")
lst=[int(val) for val in input().split()]
print("Content of lst=",lst)
psevenlst=list(filter(lambda val: val>0 and val%2==0,lst))
print("list of +ve even numbers={}".format(psevenlst))
nsoddlst=tuple(filter(lambda val: val>0 and val%2!=0,lst))
print("list of odd numbers={}".format(nsoddlst))
