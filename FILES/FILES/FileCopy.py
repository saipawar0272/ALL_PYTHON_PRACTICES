#program which will copy the content of one file into another
srcfile=input("Enter source file")
try:
    with open(srcfile,"rt") as rp: #opening src file in read mde
        dstfile=input("Enter destination file:")
        with open(dstfile,"at") as wp:
            srcfiledata=rp.read() #readinf entire data from src file
            wp.write(srcfiledata) #write srcfiledata to dest file
            print("file copied--verify")
except FileNotFoundError:
    print("sorce file not exist")