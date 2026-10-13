#program which will read the data from keyboard and write it to the file

print("ente your data ir press @ to stop:")

with open("hyd.info","at") as si:
    while(True):
        kbddata=input()
        if(kbddata!="@"):
            si.write(kbddata+"\n")
        else:
            print("data written to the file")
            break

