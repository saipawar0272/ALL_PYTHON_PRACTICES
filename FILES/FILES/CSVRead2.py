#program for creating csv file by using csv.reader()

import csv
with open("C:\\Users\\saipr\\PycharmProjects\\FILES\\citizen.csv","r") as fp:
    dictro=csv.DictReader(fp)
    for record in dictro:
       for k,v in record.items():
        print("\t{}--->{}".format(k,v))
        
