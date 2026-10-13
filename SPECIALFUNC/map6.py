#program which will multiply 2list of object

Animal=["cat","dog","human","tiger"]
Sound=["mew","bow","nothing","roar"]
animal_sound=tuple(map(lambda ani,snd:ani+'-'+snd,Animal,Sound))
print("*"*50)
print("Animal\ts\tSound\t\tResult")
print("*"*50)
for an,sn,ansn in zip(Animal,Sound,animal_sound):
    print("\t{}\t\t\t{}\t\t\t\t{}".format(an,sn,ansn))
    print("*"*50)