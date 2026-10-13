#pytyon program whichc will acccept list of positve and negative numerical  values and find squares of positive numbers

print("Enter list of values seprated by comma:")
ps={float(val):float(val)*float(val) for val in input().split(",") if float(val)>0}
print("*"*50)
for n,sn in ps.items():
    print("\t{}----->{}".format(n,sn))