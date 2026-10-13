
text = input("Enter text :")

found = False

for char in text.lower():
    if char in 'aeiou':
        found = True
        break

if found :
    print("vowel found")
else:
    print("Vowel not found")

