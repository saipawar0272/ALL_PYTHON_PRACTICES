#python program  using comprehension and anonymous without using max and min


def kvrmax(values): #balues:10,20,30
    maxv=values[0]
    for val in values:
        if(val>maxv):
            maxv=val
    return maxv

def kvrmin(values):
    minv=values[0]
    for val in values:
        if(val<minv):
            minv=val
    return minv


findmax = lambda values:kvrmax(values)
findmin = lambda values:kvrmin(values)

print("Enter list of values seprated by space:")
vals=[int(val) for val in input().split()]
print("content of list=",vals)
bv=findmax(vals)
sv=findmin(vals)

print("max({})={}".format(vals,bv))
print("min ({})={}".format(vals,sv))