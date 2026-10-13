#wap program which will filter +ve elements and -ve elements seprately

def zero(a):
    if(a==0):
        return True
    else:
        return False

def positive(x):
    if(x>0):
        return True
    else:
        return False

def negative(y):
    if(y<0):
        return True
    else:
        return False




#main program
lst=[45,89,-12,20,-26,66,-74,-4,0,5,-78,-55,-12,-166,56,4,]

a1=list(filter(zero,lst))
print("neither pos nor neg={}".format(a1))

p1=list(filter(positive,lst))
print("original elements list={}".format(lst))
print("positive elements list={}".format(p1))

n1=list(filter(negative,lst))
print("original elements listd={}".format(lst))
print("negative elements list={}".format(n1))