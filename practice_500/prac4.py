
""" list1 = ["M", "na", "i", "Ra"]
	list2 = ["y", "me", "s", "hul"]

	Output:

	[['M','y'], ['na', me'], ['i', 's'], ['Ra', 'hul']]

"""

lst1=["m","na", "i", "Ra"]
lst2=["y","me","s","hul"]

result=list(map(list, zip(lst1,lst2)))
print(result)

"""2. Write a program to add item 7000 after 6000 in the following Python List

	list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
	Output:

	[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
	"""

lst1=[10,20,[300,400,[5000,6000],500],30,40]


lst1.append([5000])
print(lst1)

lst2=lst1[2][2].append(7000)
print(lst2)


"""	candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
	no_of_items = [10,20,34,74,32]
	Write a program to show no. of items of each candy type.

	Output:

	Jelly Belly-10
	Kit Kat-20
	Double Bubble-34
	Milky Way-74
	Three Musketeers-32"""


candy_list=['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items=[10,20,34,74,32]

result=[]

for i in candy_list:
    for j in no_of_items:
        print(i,'>>',j)


"""4. Running Sum on list Write a program to print a list after performing running sum on it.

	Input:

	list1 = [1,2,3,4,5,6]
	Output:

	[1,3,6,10,15,21]
	"""


lst1=[1,2,3,4,5,6]

lst_sum=[]
total=0

for num in  lst1:
    total += num
    lst_sum.append(total)
    print(lst_sum)

"""5. You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.

	i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].

	For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

	For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

	like wise for all other elememts.

	[2,4,6,10,1]-->[22,20,16,10,23]"""


lst1=[2,4,6,10,1]

result=[]

for i in range(len(lst1)):
    total=lst1[i]

    for j  in range(len(lst1)):
        if lst1[j] > lst1[i]:
            total +=lst1[j]
    result.append(total)

print(result)

"""6. Find list of common unique items from two list. and show in increasing order

	Input

	num1 = [23,45,67,78,89,34]
	num2 = [34,89,55,56,39,67]
	Output:

	[34, 67, 89]
"""

num1=[23,45,67,78,89,34]
num2=[34,89,55,56,39,67]

result=sorted(list(set(num1) & set(num2)))
print(result)

"""7. Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.

	Input:

	['1ac21', '23fg', '456', '098d','1','kls']
	Output:

	['456', '23fg', '1ac21', '1', 'kls', '098d']"""


lst1=['1ac21', '23fg', '456', '098d','1','kls']



"""8. Write a program that can find the max number of each row of a matrix
	Example:

	Input:

	[[1,2,3],[4,5,6],[7,8,9]]
	Output:

	[3,6,9]
	"""

lst1=[[1,2,3],[4,5,6],[7,8,9]]

result=[]

for row in lst1:
    result.append(max(row))
    print(result)

"""9. Shortlist Students for a Job role Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

	Show every students record in form of tuples if matches all required criteria.
	It is assumed that there will be only one primry skill.
	If no such candidate found, print No such candidate
	Iput:
	Enter No of records- 2
	Enter Details of student-1
	Enter Student name- Manohar
	Enter Higher Education- B.Tech
	Enter Primary Skill- Python
	Enter Year of Graduation- 2022
	Enter Details of student-2
	Enter Student name- Ponian
	Enter Higher Education- B.Sc.
	Enter Primary Skill- C++
	Enter Year of Graduation- 2020

	Enter Job Role Requirement
	Enter Skill- Python
	Enter Higher Education- B.Tech
	Enter Year of Graduation- 2022
	Output

	('Manohar', 'B.tech', 'Python', '2022')"""


"""10. Write a program to find set of common elements in three lists using sets.

	Input : ar1 = [1, 5, 10, 20, 40, 80]
			ar2 = [6, 7, 20, 80, 100]
			ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

	Output : [80, 20]
	"""

arr1=[1,5,10,20,40,80]
arr2=[6,7,20,80,100]
arr3=[3,4,15,20,30,70,80,120]

result=list(set(arr1) & set(arr2) & set(arr3))
print(result)

"""11. Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.

	Input:

	Output:	Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"


	No of unique vowels-6"""

str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"


vowels=set()

for ch in str1:
    if ch in 'aeiouAEIOU':
        vowels.add(ch)

print("no of unique vowels", len(vowels))

"""	lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
	lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
	Output:

	[9, 10, 4, 5]"""


lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}


result=list(set(lst1) & set(lst2) )
print(result)

"""13. Convert a list of Tuples into Dictionary.
	Example 1:

	Input:

	[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
	Output:

	{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
	Example 2:

	Input:

	[('A', 1), ('B', 2), ('C', 3)]
	Output:

	{'A': [1], 'B': [2], 'C': [3]}"""


lst1=[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
result=dict(lst1)
print(result)

lst2=[('A', 1), ('B', 2), ('C', 3)]
result1=dict(lst2)
print(result1)

"""14. Write a Python function that takes a list and returns a new list with unique elements of the first list.
	Exercise 1:

	Input:

	[1,2,3,3,3,3,4,5]
	Output:

	[1, 2, 3, 4, 5]"""

lst1=[1,2,3,3,3,4,5]
result=set(lst1)
print(result)

""" 
17. Write a Python function to concatenate any no of dictionaries to create a new one.
	Sample Dictionary :
	dic1={1:10, 2:20}
	dic2={3:30, 4:40}
	dic3={5:50,6:60}
	Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

result={}

result.update(dic1)
result.update(dic2)
result.update(dic3)

print(result)

#---------------------------------------------------------------------------------------------------------------------------------------

#1. Write a Python function to find the maximum of three numbers.


"""def maxx():
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    c=int(input("enter number:"))

    d=max(a,b,c)
    print("highest",d)

maxx()"""

"""2. Write a Python function to sum all the numbers in a list.

	Sample List : (8, 2, 3, 0, 7)
	Expected Output : 20"""


def summ():
    lst1=[8,2,3,0,7]
    print(sum(lst1))

summ()

"""3. Write a Python function to multiply all the numbers in a list.

	Sample List : (8, 2, 3, -1, 7)
	Expected Output : -336"""

def multiply():
    lst1=[8,2,3,-1,7]
    result=1
    for num in lst1:
        result *= num
        print(result)

multiply()

def summ():
    lst1=[8,2,3,0,7]
    result=0
    for num in lst1:
        result += num
        print(result)
summ()

#------------------------

"""	
4. Write a Python function to reverse a string. 

	Sample String : "1234abcd"
	Expected Output : "dcba4321"
	"""

def revers(s):
    return s[::-1]
print(revers("1234abcd"))


def reverse():
    return s[::-1]
print(revers("abcd1234"))


"""5. Write a Python function to check whether a number falls within a given range.
"""

"""def check():
    b=int(input("enter number:"))
    lst1=[5,6,8,9]
    if b in lst1:
        print("number exists")
    else:
        print("num not")

check()"""

"""
6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
	Sample String : 'The quick Brow Fox'
	Expected Output :
	No. of Upper case characters : 3
	No. of Lower case Characters : 12"""


def count(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("no of upper char",upper)
    print("no of lower char",lower)

count("The quick Brow Fox")

"""7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

	Sample List : [1,2,3,3,3,3,4,5]
	Unique List : [1, 2, 3, 4, 5]"""


def sample():
    lst1=[1,2,3,3,3,3,4,5]

    lst2=list(set(lst1))
    print(lst2)

sample()

"""8. Write a Python function that checks whether a passed string is a palindrome or not.

	Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.0"""

def palindrome():

    lst=input("enter word:")

    if lst==lst[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

palindrome()

"""9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

	Sample Items : green-red-yellow-black-white
	Expected Result : black-green-red-white-yellow"""

def hypen():
    lst1=["green-red-yellow-black-white"]
    lst2=(sorted(lst1))
    print(lst2)

hypen()

"""10. Write a Python program to detect the number of local variables declared in a function.
"""

def cout():
    a=10
    b=20
    c=a+b

    print("local variable",locals())
    print("len of local",len(locals()))

cout()

"""11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

	Sample Output:
	25
	48"""

def multiplly():
    b= lambda x,y:x*y
    print(b(5,9))
    add_15= lambda x:x+15
    print(add_15(10))

multiplly()

"""	
12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

	Sample Output:
	Double the number of 15 = 30
	Triple the number of 15 = 45
	Quadruple the number of 15 = 60
	Quintuple the number 15 = 75"""

def func():
    a=lambda x:x*15
    print(a(2))
    b=lambda x:x*15
    print(b(3))
    c=lambda x:x*15
    print(c(4))

func()

"""13. Write a Python program to sort a list of tuples using Lambda.

	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""

def sortt():
    lst1=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

    sorted_list=sorted(lst1, key=lambda x:x[1])
    print(sorted_list)

sortt()

"""14. Write a Python program to sort a list of dictionaries using Lambda.

	Original list of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
	Sorting the List of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]"""


def dic():
    lst1=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    lst2=sorted(lst1, key=lambda x:x['make'])
    print(lst2)

dic()

"""15. Write a Python program to filter a list of integers using Lambda.

	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Even numbers from the said list:
	[2, 4, 6, 8, 10]
	Odd numbers from the said list:
	[1, 3, 5, 7, 9]	"""

def fil():
    lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even= list(filter(lambda x:x%2==0, lst1))
    odd = list(filter(lambda x:x%2==1,lst1))
    print("even",even)
    print("odd",odd)

fil()

def mapp():
    lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    mapp= list(map(lambda x:x**2,lst1))
    print(mapp)

mapp()

"""	
16. Write a Python program to square and cube every number in a given list of integers using Lambda.

	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Square every number of the said list:
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	Cube every number of the said list:
	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]"""


def mapp():
    lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mapp= list(map(lambda x:x**2,lst1))
    mapp1= list(map(lambda x:x**3,lst1))
    print(mapp)
    print(mapp1)

mapp()

"""18. Write a Python program to find if a given string starts with a given character using Lambda.
"""

def starts():
    string=input("enter string :")
    ch=input("enter starting char")

    start_with = lambda x,y: x.startswith(y)

    if start_with(string,ch):
        print("yes string start with given char")
    else:
        print("no,doesn't start with char")

starts()

"""19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

	Original arrays:
	[-1, 2, -3, 5, 7, 8, 9, -10]
	Rearrange positive and negative numbers of the said array:
	[2, 5, 7, 8, 9, -10, -3, -1]"""


def arrange():
    lst1=[-1, 2, -3, 5, 7, 8, 9, -10]
    lst2=sorted(lst1, key=lambda x:x<0)
    print(lst2)

arrange()

"""20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

	Original arrays:
	[1, 2, 3, 5, 7, 8, 9, 10]
	Number of even numbers in the above array: 3
	Number of odd numbers in the above array: 5
	"""

def lam():
    lst1=[1,2,3,5,7,8,9,10]
    lst2= len(list(filter(lambda x: x%2==0,lst1)))
    lst3= len(list(filter(lambda x:x%2==1,lst1)))
    print("even",lst2)
    print("odd",lst1)

lam()

"""21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

	Orginal list:
	[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
	Numbers of the above list divisible by nineteen or thirteen:
	[19, 65, 57, 39, 152, 190]
	"""

def divisible():
    lst1=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

    lst2= list(filter(lambda x:x%13==0,lst1))
    lst3= list(filter(lambda x:x%19==0,lst1))
    print(lst2)
    print(lst3)

divisible()

""""""




    


