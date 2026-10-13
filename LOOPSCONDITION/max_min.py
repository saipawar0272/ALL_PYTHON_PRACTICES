#wap which will find max and min elements from the given list of elements

def findmaxmin(lst):
        maxelement=max(lst)
        minelement=min(lst)
        return maxelement,minelement

def dispresult(xl,he,se):
    print("element of list:")
    for v in xl:
        print("\t{}".format(v))
        print("max element={}".format(he))
        print("min of element={}".format(se))

#main program

lst=[10,56,87,-87,-23,-45,-12,65,44]
max,min=findmaxmin(lst)
dispresult(lst,max,min)