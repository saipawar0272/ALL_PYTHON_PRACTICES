#program to demonstrate variable length argument or parameter
def dispval(sno,sname,*a,city="hyd"): #*a will be preceded as variable length argument

   print("*"*50)
   print("Student Number=",sno)
   print("Student Name=",sname)
   print("student city=",city)


   s=0
   for v in a:
       print("{}".format(v),end=" ")
       s=s+v
       print()
       print("sum=",s)
#main program
dispval( 100,"sai",10,20,30,40,50)
dispval(200,"ramesh",10,20,30,40)
dispval(300,"ganesg",10,20,30)
dispval(400,"russow",10,20)
dispval(500,"ASCII",10)