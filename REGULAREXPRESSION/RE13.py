#python program which will extract name of the students from given text by using regular expressions

import re

gd="Rossum is the father of python, Travis is the developer of numpy, kinney us the developer of pandas and Ritche is the father of NLP "
sp="[A-Z][a-z]+"
nameslist=re.finditer(sp,gd)
for names in nameslist:
    print(names.start(),names.end(),names.group())