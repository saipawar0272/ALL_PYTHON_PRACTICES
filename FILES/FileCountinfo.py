
try:
    filename=input("Enter Any file:")
    with open(filename,"rt") as si:
         lines=si.readlines()
         nl=0
         nw=0
         nc=0
    for line in lines:
                 nl=nl+1
                 nw=nw+len(line.split())
                 nc=nc+len(line)

    else:
                   print("*"*50)
                   print("number of lines=",nl)
                   print("number of words=",nw)
                   print("number of line=",nc)
except FileNotFoundError:
                   print("file not exist")

