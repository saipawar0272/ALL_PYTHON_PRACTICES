#program for demonstrating keyword arguments
def disp(A,B,C,D):
    print("\t{}\t{}\t{}\t{}".format(A,B,C,D))

#main program
print("*"*50)
print("\tA\tB\tC\tD")
print("*"*50)
disp(10,20,30,40) #function call with positional arguments
disp(A=10,C=30,D=40,B=20) #function call with keyword arguments
disp(D=40,C=30,B=20,A=10) #function call with keyword arguments
disp(10,20,D=30,C=40) #function call with keyword and positional arguments
disp(20,30,10,40)
print("*"*50)