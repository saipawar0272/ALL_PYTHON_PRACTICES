#program for extracting marks and names from given data by using regular expression

import re
gd="Rossum is the father of python and marks=89, Travis is the developer of numpy and marks=85, kinney us the developer of pandas and marks =74 ,Ritche is the father of NLP and marks=59"
try:

        filedata=gd
        nameslist=re.findall("[A-Z][a-z]+",gd)
        markslist=re.findall(r"\d{2}",gd)
        print("*"*50)
        print("names\t\tmarks")
        for names,marks in zip(nameslist,markslist):
            print("{}\t{}\t".format(names,marks))

except FileNotFoundError:
    print("file not found")