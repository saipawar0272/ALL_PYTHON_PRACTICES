#wap program to understand scope of global variable

crs="PYTHON" #global variable can be accessed in all function definitions

def learnds():
    print("to learn data science we need programming lan:{}".format(crs))

def learniot():
    print("to learn iot we nees programmong lang:{}".format(crs))

def learnpyton():
    print("to learn python we nned programming lang:{}".format(crs))

#main program
learnds()
learniot()
learnpyton()