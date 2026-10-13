#program to demonstrate local  an global variable

def learnAI():
    sub1="AI"  #here sub1 is called local variable
    print("to develope '{}' language we use'{}' labguage".format(sub1,lang))

def learnML():
    sub1="ML"
    print("to develope '{}' we use '{}' python language".format(sub1,lang))

lang="python" #here lang is called global variable,,always define global variable before the function call
learnAI()
learnML()