# decide word is vowel or not
word=input("Enter a word:")
res=" not VOWEL"
for ch in word:
    if ch.lower() in ['a','e','i','o','u']:
        res="VOWEL"
        break
    print("{} is {}".format(word,res))