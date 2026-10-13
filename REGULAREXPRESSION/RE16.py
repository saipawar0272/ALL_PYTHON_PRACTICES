#python program which will extract mail id from given data using regular expression

import re

sd="Sai mail id is =sai@gmail.com, Gana mail id is =gana@gmail.com , Sakshi mail id is sakshi@gmail.com, Anup mail id is anup@gmail.com"

try:
    filedata=sd
    mailslist=re.findall(r"\S+@\S+",filedata)
    print(mailslist)
except FileNotFoundError:
    print("file not found")

