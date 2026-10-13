def show(*n): #here value n is called
    for val in n:
        print("{}".format(val), end=" ")
        print("\n")

def disp(*nav):
    for val in nav:
        print("{}".format(val), end=" ")
        print("\n")

#main program

show(10)
show(10,20,'abvc')
show(30,40,50,'def')


disp(10)
disp(10,20)
disp(30,40,50)
disp(60,70,'xyz','def')

