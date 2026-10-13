
numbers = [56,89,52,4,66,23,89,965,52,65,-8,-56,-45,-885,1,2,-6,-9,10]


positive = []
negative = []

for i in numbers:
    if i >= 0:
        positive.append(i)
    else:
        negative.append(i)

print("positive numbers",positive)
print("negative numbers",negative)
