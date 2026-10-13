#program to calculate total marks of students who studied in diffrent classes with diffrent subjects
def findtotalmarks(sno,sname,batch,cls, *vals, city="hyd", **submarks):

    print("variable length of arguments:{}".format(vals))
    print("*"*50)
    print("student name={}".format(sno))
    print("student name={}".format(sname))
    print("student batch={}".format(batch))
    print("student class={}".format(cls))
    print("student living city={}",city)
    print("\tsubject\t\tMarks")
    totmarks=0
    for subject,marks in submarks.items():

        print("\t{}\t\t{}".format(subject,marks))
        totmarks=totmarks+marks
        print("TOTAL MARKS={}".format(totmarks))
    print("*"*50)

findtotalmarks(100,"sai","X", 10,eng=89,math=85,sci=95,history=86,geo=96)
findtotalmarks(200,"ramesh","XII", 12,English=89,Arts=96,Math=88,Science=99)
