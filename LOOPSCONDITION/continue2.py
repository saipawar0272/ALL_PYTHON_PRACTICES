#wap which will display positive and negative numbers seprately

lst=[89,66,56,85,-74,-5,-96,-12,-74,20]

for val in lst:
    if(val<=0):
        continue
    print("\t",val)
print("==============================")

for val in lst:
    if(val>=0):
        continue
    print("\t",val)