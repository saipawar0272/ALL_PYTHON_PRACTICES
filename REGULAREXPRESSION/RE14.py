#python program which will retrieve marks of the students from given text

import re
gd="Rossum is the father of python marks=96, Travis is the developer of numpy marks=89, kinney us the developer of pandas marks=45 and Ritche is the father of NLP maeks=56"
sd=r"\d{2}"
markslist=re.findall(sd,gd)
nameslist=re.findall("[A-Z][a-z]+",gd)
for marks in markslist:
    print(marks)
    print("*"*50)
for names in nameslist:
    print(names)