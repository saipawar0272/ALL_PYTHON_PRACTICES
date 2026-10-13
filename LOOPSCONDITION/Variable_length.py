#wap which will demonstrate the use of variable lenght parameter

def show(*n):  #here *n is called varaible lenght parameter whose type is tuple
    for val in n:
        print("{}".format(val),end=" ")
    print("\n")

def disp(*nav):  #here nav is called variable lenght parameter
    for val in nav:
        print("{}".format(val),end=" ")
    print("\n")

#main program

#n-similar function calls with variable number of values

show(10)
show(12,20)
show('java','python',56)
show(10,20,30,'java','python')
show()

#n-similar function calls with variable number of values

disp(56,78)
disp(852)
disp("java",'pyton',89,74)
disp(85,96,96,'java','pyton')
