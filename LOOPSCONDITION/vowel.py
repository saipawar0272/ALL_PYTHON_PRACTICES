#write python program which will accept word decide whether it is vowel or not
word=input("Enter a word:")
res="VOWEL"
for ch in word:
    if ch in ['a','e','i','o','u']:
        res="VOWEL"
        break
        print("{} is {}".format())