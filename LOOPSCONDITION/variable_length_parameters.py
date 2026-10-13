def show(*n): #here *n is called variable lenght parameter name whose type is tuple
    for val in n:
        print("{}".format(val),end=" ")
    print("\n")


def disp(*n):#here *n is called variable length parameter name whose type is tuple
    for val in n:
        print("{}".format(val),end=" ")
    print("\n")

#main program
#n-similar function calls with variable number of values
show(10)
show(12,20)
show(10,20,30)
show('kvr','python','java')
show()
print("*"*20)
disp(20)
disp(20,30)
disp(30,40,50)
disp('kvr','sai','ram')
disp()