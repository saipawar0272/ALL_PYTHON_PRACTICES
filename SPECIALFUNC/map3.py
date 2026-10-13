#program which will accept list of numerical values and obtain squares and sqaure roots

print("enter list of values:")
values=[float(val) for val in input().split()]
#compute square root
sqroots=list(map(lambda val:val**0.5,values))
#compute squares
squares=list(map(lambda val:val**2,values))
print("*"*50)
print("Original value\t\tsquare root")
print("*"*50)
for on,sqt in zip(values,sqroots):
    print("\t{}\t\t\t{}".format(on,sqt))
    print("="*50)

print("original vlue\t\tsquares")
print("*"*50)
for on,sqt in zip(values,squares):
    print("\t{}\t\t\t{}".format(on,sqt))
    print("="*50)
