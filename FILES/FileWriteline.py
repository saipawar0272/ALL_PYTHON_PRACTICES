#program for demonstrating writing the data to the file
x=[100,"python",78.23,"sai",
{10:"sai",20:"ganesh",30:"django"} ]
with open("stud.data","a") as fp:
    fp.writelines(str(x) +"\n")
    print("data written to the file")