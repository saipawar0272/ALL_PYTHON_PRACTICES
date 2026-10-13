#python program which will create dynamic csv file .

import csv

csvfilename=input("Enter csv filename with an extension .csv:")
noh=int(input("Enter how many header name you want in '{}' file:".format(csvfilename)))
if(noh<=0):
    print(" {} invalid header names ,must contain atleast 1 header file")
else:
    colnames=[]
    for i in range(1,noh+1):
        col=input("Enter {} Col Name for {}:".format(i,csvfilename))
        colnames.append(col)
    else:
        #print(colnames)
      nor=int(input("Enter how many records you want to enter for {} file:".format(csvfilename)))
    if(nor<=0):
        print("{} invalid number of records for {}".format(nor,csvfilename))
    else:
        records=[] #outer list to take record as inner list
        for i in range(1,nor+1):
            print("*"*50)
            print( " Enter {} Record:".format(i) )
            record=list() #inner list for single record
            for j in range(len(colnames)):
                val1=input("Enter value for {}:".format(colnames[j]))
                record.append(val1)
            else:
                records.append(record) #adding single record to outer list
        else:
             with open(csvfilename,'a') as fp:
                 wo=csv.writer(fp)
                 wo.writerow(colnames)
                 wo.writerows(records)
                 print("{} Created Successfully--very".format(csvfilename))