#program for demonstrating variable length arguments
def dispvals1(a,b,c,d,e): #function def-1
    print(a,b,c,d,e)
def dispvals2(a,b,c,d): #function def-2
        print(a,b,c,d)
def dispvals3(a,b,c):
            print(a,b,c)
def dispvals4(a,b):
                print(a,b)
def dispvals5(a):
                    print(a)


#main program
dispvals1(10,20,30,40,50) #function call with 5-positional arguments
dispvals2(10,20,30,40)  #function call with 4 positional arguments
dispvals3(10,20,30)
dispvals4(10,20)
dispvals5(10)