"""
Class Examples : 16/07/21
====================

>>> print("hlo world")
hlo world
>>> 
>>> 
>>> a = 10
>>> print(a)
10
>>> ca$h = 10
SyntaxError: invalid syntax
>>> 123this = 10
SyntaxError: invalid syntax
>>> this123 =10
>>> this123
10
>>> _this = 10
>>> _this
10
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> True = 10
SyntaxError: cannot assign to True
>>> trues =10
>>> tures
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tures
NameError: name 'tures' is not defined
>>> trues
10
>>> total = 20
>>> TOTAL = 30
>>> total
20
>>> TOTAL
30
>>> def 10
SyntaxError: invalid syntax
>>> class 10
SyntaxError: invalid syntax
>>> a =10
>>> 
>>> 
>>> 
>>> 
>>> 
============================== RESTART: /Users/jai/Desktop/test.py =============================
hello world
13579111315171921232527293133353739414345474951535557596163656769717375777981838587899193959799
>>> 
============================== RESTART: /Users/jai/Desktop/test.py =============================
hello world
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 
>>> 
>>> 
>>> this = 10
>>> print( type(this) )
<class 'int'>
>>> b=10.5
>>> print(type(b))
<class 'float'>
>>> c = 10+2j
>>> print(type(c))
<class 'complex'>
>>> d =True
>>> print(type(d))
<class 'bool'>
>>> d = None
>>> d
>>> 


print("hello world")

for i in range(1,100,2):
     print(i,end=' ')

name = input("Enter your name:")
if name == "adithi":
    print("hello",name)
else:
    pass    

# out 
# Enter your name:adithi
# hello adithi


=================
Terminal command    :
=================
1. For windows :
  1. Python version check on cmd   python --version, and py -V
  2. Python open shell on cmd(Command Prompt) :  python, and py  
2. For macOS : 
  1. for python2 version check  python2 --version
  2. for python3 version è python3 —version
  3. for python2 open shell on terminal  python2, python
  4. for python 3 shell on terminal python3
3. For linux/Ubuntu/Chrome os :
  1. for python2 version python2 --version
  2. for python3 version python3 --version
  3. for python2 open shell on terminal   python2 ,  python
  4. for python 3 shell on terminal python3


====================================
How to run your python file on terminal and cmd :

For windows	:  python file_name.py
For Mac/linux/chrome os : python3 file_name.py

python_classes % python3 test.py 
hello world
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 % 

How to move one dir to another dir using command :

cd=change dir
pwd = present	working dir
ls=list of all dir

"""

"""
13/08/31
=============
dict data types :
1. duplicate key is not allow
2. value will be duplicate
3. key value pair combinations
eg :

d = {101:"this",130:"not is", 102:"adithi"}

# 1. creation empty dict
d = {}
print(type(d)) #<class 'dict'>

# 2. using inbuilt function we can also create dict 

d2 = dict()
print(type(d2)) #<class 'dict'>

d3 = {1:"one",2:"two",3:"three"}

# 1. for accessing value using key like -: 1,2,3 
# value is : one, two, three
print(d3[2]) # two

# 2 .for inserting new value with new key
d3[42] = "new value" 
print(d3) # {1: 'one', 2: 'two', 3: 'three', 42: 'new value'}

# 3. for replacing value with key
d3[2]="new two"
print(d3) #{1: 'one', 2: 'new two', 3: 'three', 42: 'new value'}

# for printing whole keys
print(d3.keys()) # dict_keys([1, 2, 3, 42])

# for printing whole values
print(d3.values()) #dict_values(['one', 'new two', 'three', 'new value'])

# other way to define dict :

info = {
    "name": "deepti",
    "age" : 10,
    "phone" : 123456,
    "country": "USA",
}


note :
=========

=   (assinging value) ,a = 10 
==  comparing two value

!
@
~ ->tindle
# -> has tag
$ -> doller 
% -> percentage
^ -> power
& -> and 
() -> small braces
{} -> curly 
/ -> forward 
\ -> bakcward
* -> multi
[] -> square barces
. -> for accessing current variable
: -> colon
; -> semi colon

& =and  ^=or  !=not ( bit wise operator)


while True:
    age1 = int(input("Enter your age :"))
    age2 = int(input("Enter your age :"))
    if age1 == age2:
        print("welcome to python prog")
    else:
        print("invalid input try again")    
    

output test case :
{1: 'one', 2: 'two', 3: 'three', 42: 'new value'}
Enter your age :10
Enter your age :20
invalid input try again
Enter your age :20
Enter your age :20
welcome to python prog

"""

"""
Homework :
=============
Python dict :
1. Select correct ways to create an empty dictionary
	•	sampleDict = {}
	•	sampleDict = dict()
	•	sampleDict = dict{}

2. Select the all correct way to remove the key marks from a dictionary
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

3. What is the output of the following dictionary operation
dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)

4. What is the output of the following code
dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)

5. Dictionary keys must be immutable
	•	True
	•	False

6. What is the output of the following dictionary operation
dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)

7. Select the correct ways to get the value of marks key.
student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}



"""

"""
Aug/18/21 class example:
========================

Important functions of dictionary:

1. len()
Returns the number of items in the dictionary 

2. clear():
To remove all elements from the dictionary 

3. get():
To get the value associated with the key

4. pop():

d.pop(key)
 It removes the entry associated with the specified key and returns the corresponding value

  1. If the specified key is not available then we will get KeyError

5. items():
It returns list of tuples representing key-value pairs. 
"""

# d = {1:"one", 2:"two", 3:"three"}
# for k,v in d.items():
#     print(k, "=======" ,v)

"""
1 ======= one
2 ======= two
3 ======= three
"""

# [()] ==> list of tuple
# {()} == set of tuple 

# 8. copy():
# To create exactly duplicate dictionary(cloned copy) d1=d.copy()

# d = {1:"one", 2:"two", 3:"three"}
# c = d.copy() #  {1:"one", 2:"two", 3:"three"}
# print(c)
# print(d.pop(1))
# print(c)

# {1: 'one', 2: 'two', 3: 'three'}
# one
# {1: 'one', 2: 'two', 3: 'three'}


# Dictionary Comprehension:

# for printing even no : # for even no : 0,2,4..N
# dc = { i:i*2 for i in range(0,20) }
# print(dc)

# for k,v in dc.items():
#     print(k,"=====",v)


# s = "this is string"
# print(s)

# prob  : this is one 
#       this is second line

# s1 = "this is one\nthis is second line"
# print(s1)


"""
if outerside double quote then inside only applicable single quote
if outerside single quote then innerside only applicable double quote

"""
# prob : "this is one 'this' is second line"

# s2 = "this is one 'this' is second line"
# print(s2)

# this is one 'this' is second line


# prob : 'this is one "this" is second line'

# s3 = 'this is one "this" is second line'
# print(s3)

# this is one "this" is second line

"""
homework 18/aug/21 : 
====================

1. using dict how to print odd and even number and print all keys and values
2. using list how to print odd and even number 
3. using tuple how to print odd and even number 
4. using set how to print odd and even number 

hint : logic same for all data types
"""

"""Aug/20/21 class example"""

# for odd and even num:

# # 1. way
# l = [0,1,2,3,4,5,6,7,8,9,10]
# # for even
# print(l[::2]) #[0, 2, 4, 6, 8, 10]

# # for odd
# print(l[1::2]) # [1, 3, 5, 7, 9]

# 2. way 
# for even
# for i in range(0,20,2):
#   print(i,end=" ")

# for odd : 1 3 5 7 9 11 13 15 17 19
# for i in range(1,20,2):
#   print(i,end=" ")

# 3. way : for even no:  if no is divisible by 2 so that is even no

"""
>>> 12%2!=0 # 0!=0 --> False
False
>>> 13%2!=0 # 1 != 0 --> Ture
True
>>> 
"""

# n1 = int(input("Enter any int no:"))
# if n1%2==0:
#   print("Even no is:",n1)


# 4. way to printing odd  no: if no is not divisible by 2 so that is odd no

# n1 = int(input("Enter any int no:"))
# if n1%2!=0: # 12%2!=0 
#   print("odd no is:",n1)

  
"""
Enter any int no:13
odd no is: 13
"""  
   
  
"""Operator"""  

# floor division : // (it's depend's on the input )
"""
1. if input is int -->then output will we int 
2. if input is float -->then output will we float 
  note : it's always ignore decimal part

"""
# 1. case :  int input
# print(10//2) # 5

# # 2. case :  float input
# print((21//2.5)) #  8.0

# # 3. case :  float input
# print((21.5//2.5)) # 8.0

"""
5
8.0
8.0
"""

""" Realational operator 25/Aug/21"""
# 1.  output will be true or false

# for int value
# print(10 > 20) # Ture
# print(10 < 20) # False

# for str
# print("rahul" > "deepti") # Ture
# print("rahul" >= "r2hul") # Ture

"""
unicode of char is :
for  lower case : 97 to 122 --> 97 to 123 
for upper case : 65 to 90 --> 65 to  91
"""
# for i in range(97,123):
#   print(chr(i),end=" ")  

# for i in range(65,91):
#   print(chr(i),end=" ")

# 2 . equality operator :  ==  ,!=
# a = 10
# print(a)

# b = 10
# c = 20
# print(b == c) #False

"""
= -> for assinging value
==  -> for comparing two value or conditions
!=  -> not equal 
""" 

""" eg for not equal :

name = input("Enter your name :")
if name != "adithi":
  print("welcome to python with jai") 
else:
  print("else block executed ") 
  
""" 

"""
logical operator : 
and  --> &
or  --> ||
not --> !
"""

"""
# (and) operator : 
  if both statment is True then output will be true otherwise false
"""
# while True:
#   name = input("Enter your name :")
#   passwd = input("Enter your passwd :")

#   if name == "adithi" and passwd == "adithi123@":
#     print("Name is:",name,"and your passwd is:",passwd)
#   else:
#     print("Invalid input try again")  
    
"""
Enter your name :adithi
Enter your passwd :adithi4321@
Invalid input try again
"""    

"""
# 2  (or) operator : 
  if at least one statement(condition) is True then output will be true ohterwise
  false
"""

# while True:
#   name = input("Enter your name :")
#   passwd = input("Enter your passwd :")
#   if name == "adithi" or passwd == "adithi123@":
#     print("Name is:",name,"and your passwd is:",passwd)
#   else:
#     print("Invalid input try again") 

""" output :
Enter your name :adithi
Enter your passwd :adithi123@
Name is: adithi and your passwd is: adithi123@

Enter your name :adithi
Enter your passwd :
Name is: adithi and your passwd is: 

Enter your name :
Enter your passwd :adithi123@    
Name is:  and your passwd is: adithi123@

Enter your name :
Enter your passwd :
Invalid input try again
"""    

"""27/Aug/21 class example"""
# 1 .for min of 3 numbers :
# min ---> 1,4,6,20,45,3  --> min no is : 1

# a = int(input("Enter no 1:"))        
# b = int(input("Enter no 2:"))        
# c = int(input("Enter no 3:"))

# # a b c ==>   a<b  , a<c, b<c  
# # 1. I way
# min = a if a<b and a<c else b if b<c else c
# print(min)

# # 2 II way
# if a<b and a<c:
#   print(a)  
# elif b<c:
#   print(b)
# else :
#   print(c)  
  

# 2. for max of 3 numbers : 
#  max ---> 3,5,6,3,5,7 --> max no is : 7 

# a b c ==>   a>b  , a>c, b>c  
# 1. I way
# a = int(input("Enter no 1:"))        
# b = int(input("Enter no 2:"))        
# c = int(input("Enter no 3:"))

# I way
# min = a if a>b and a>c else b if b>c else c
# print(min)

# #  II way
# if a>b and a>c:
#   print(a)  
# elif b>c:
#   print(b)
# else :
#   print(c) 
  


"""01/Sep/21 class example
============================
"""

"""
Assignment Operators:
====================
We can use assignment operator to assign value to the variable.
Eg: x = 10

 We can combine asignment operator with some other operator to form compound
 assignment operator.
 Eg: x += 10 ====> x = x+10
 The following is the list of all possible compound assignment operators in Python
+= 
-=
*=
/=
%= 
//= 
**=
&=
|=
^=
>>=
<<=
"""
# # Eg:
# x=10
# x+=20
# print(x) #30

"""
num = int(input("Enter any type of input like list,tupel,set,float:"))
print(num)

num = eval(input("Enter any type of input like list,tupel,set,float:"))
print(num)

"""

# q.2 :  avg of 5 numbers 
""" 
1 step :      1,2,3,4,5 ===> 1+2+3+4+5 = 15
2 nd step :   sum of all num / no of elements 
3rd step :    avg =  15/5 = 3
"""

# num = eval(input("Enter 5 elements/numbers :"))
# sum = 0

# for i in num:
#   sum = sum+i 
  
# avg = sum / len(num)

# print("sum of all num is:",sum)
# print("Avg for all elements is:",avg)

"""
Enter 5 elements/numbers :[1,2,3,4,5]
sum of all num is: 15
Avg for all elements is: 3.0
"""

# 3. write a program to check username ,password, age, phone_no using if statements:
# username = input("Enter your name :")
# password = input("Enter your password:")
# age = int(input("Enter your age:"))
# phone_no = int(input("Enter your phone_no:"))

# if username == "adithi" and password == "adithi123@" and age == 15 and phone_no == "+912345":
#   print("Hlo user your :",username,"and your age is:",age,"your cell phone no is:",phone_no) 
# else:
#   print("Your input is invalid try again")

"""
output : 
========

Enter your name :adithi
Enter your password:adithi123@
Enter your age:15
Enter your phone_no:+9123  
Your input is invalid try again

"""

""" 02/Sep/21 """

# Assignment operator : = , += ,-=

# a = 10 # assigning value
# a += a # a = a+a  ==> # increasing value with one
# print(a)

# a = 10 # assigning value
# a = a+10 # a = a+a  ==> # increasing value with one
# print(a)

# b = 10
# b -= b # b = b-b
# print(b)

# Ternary operator :

# normal way 
# num1 = int(input("Enter no 1:"))
# num2 = int(input("Enter no 2:"))

# if num1 > num2:
#   print("Num1 is greater")
# else:
#   print("num1 is lessthan of num2")  
  
# ternary operator : program for lessthan or greater than

# num1,num2 = [ int(i) for i in input("Enter two no:").split(":")]
# print("num1 is greater") if num1>num2 else print("num1 is lessthan of num2")  

""" 08/Sep/21 """

# 3.Given two integer numbers return their (multiplications). 
#     If the multiplications is greater than 1000, then return their sum

# while True :
#   a = int(input("Enter 1st no:"))
#   b= int(input("Enter second no:"))
#   mul = a*b

#   if mul <= 1000:
#     print("Multiplication of two no is:",mul)
#   else:
#     print("sum of two no is:",a+b)   
 

"""
Enter 1st no:10
Enter second no:20

Multiplication of two no is: 200


Enter 1st no:30
Enter second no:40  ==>30*40 ==1200 <= 1000

sum of two no is: 70
"""


# 3.Given three integer numbers return their (multiplications). 
#     If the multiplications is greater than 1000, then return their sum

# note : take three input from user side/keyword using ternary operator :


"""  10_Sep_21 """

"""    
1. Inentifier
2. data types
3. operators
4. some programs : average, grading system,min,max,odd & even no,
  cal program, 
  
5. How to take input from user diffrent  case : for int, for boolean,for float  
6. how to print a to z in lowercase 
7. how to print A to Z in uppercase
8. slicing

"""

# True or False ==> boolean
# age = int(input("Enter your age :"))
# status = bool(input("Enter your status True or False :"))
# name  = input("Enter your name :")
# sallary = float(input("Enter your sallary : "))


# to print A to Z uppercase
#  65 + 25 ==> 90 
#  chr() ==> for converting unicode format
#  end = for printing outupt with one line / horizonatally
# range(start,end-1,step)


# for i in range(65,91):
#   print(chr(i),end=" ")


# to print a to z uppercase
#  97+25 = 122

# for i in range(97,123):
#   print(chr(i),end=" ")

# 1. Write a programm that ask for a number to the user and clasifies it:

# number <2 SMALL
# number <10 MEDIUM
# number rest LARGE


"""
Control Statements  or Flow Control: 
=====================================
definitions: 
Flow control describes the order in which statements will be executed at runtime.

1. if
2. if-else
3. if-elif-else

"""
# 1. if : syntax : only for one conditions

# name = input("Enter your name :")
# if name == "adithi":
#   print("hello",name)
  
# """
# Enter your name :adithi
# hello adithi
# """  

# 2. if-else : only for the two conditions
# name = input("Enter your name :")
# if name == "adithi":
#   print("hello",name)
# else:
#   print("invalid name pls try")  

"""
Enter your name :adithi
hello adithi
"""
  
# 3. if-elif-else :
"""
if is sections --> A --> print msg --> welcome to sections A
elif is sections --> B --> print msg --> welcome to sections B
elif is sections --> C --> print msg --> welcome to sections C
else print some msg

= --> assign value 
== --> comparing value

if the user input A or a then print msg
if the user input B or b then print msg

"""

# while True:
#   sections = input("Enter your name :") 
#   # if sections == "A" or "a" :
#   if sections == "A" or sections == "a" :  
#     print("welocme to sections",sections)
#   elif sections == "B" or "b":
#     print("welocme to sections",sections)
#   elif sections == "C" or "c":
#     print("welocme to sections",sections)
#   else:
#     print("Invalid input try again")
       
    
"""
1: case input and ouput :
Enter your name :A
welocme to sections A
Enter your name :B
welocme to sections B
Enter your name :C
welocme to sections C

2. case : input and output :
Enter your name :A
welocme to sections A
Enter your name :b
welocme to sections b
Enter your name :c
welocme to sections c
Enter your name :C
welocme to sections C
"""    
    
# 2. Iterative Statements :    

# 1 . for loop 

# name = "adithi"
# for i in name:
#   print(i) 
  
"""
a
d
i
t
h
i
"""  

"""
case : 
ls = [1,2,3,4,5]  ==>15
"""
# ls = [1,2,3,4,5]
# sum=0
# for x in ls: 
#   sum = sum+x 
#   # sum = 0+1 = 1, sum = 1+2 = 3, sum = 3+3=6, sum = 6+4 = 10, sum = 10+5 = 15
#   print("sum of list is:",sum)
  
"""
sum of list is: 1
sum of list is: 3
sum of list is: 6
sum of list is: 10
sum of list is: 15
"""  
  
# from pyfunctions import ap


# ap()
# ap()
# ap()

# """50 -10
# 50 -10
# 50 -10"""


"""24/03/22"""

# 1. Print odd and even no using continue statements.
# odd --> 1,3,5...
# even --> 2,4,6...
# while statement
# continue -->
"""
< --> 9
<= --> 10
"""
# # even 
# n = 0 
# while n < 10: 
#   n+=1
#   if n%2 != 0: 
#     continue 
#   print(n)

# # odd 
# n = 0 
# while n < 10: 
#   n+=1
#   if n%2 == 0: 
#     continue 
#   print(n)

# 2. What are variable-length arguments described with an example?

# def add(a,b,c):
#   sum = a+b+c
#   print("sum is :",sum)

# add(10,20,30)
# TypeError: add() takes 3 positional arguments but 4 were given

#  n num parameter while we are calling our functions:
# def sum(*n):
#   total=0
#   for n1 in n:
#     total=total+n1
#   print("The Sum=",total)

# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30,40)
# sum(10,20,30,40,10,20)

"""output :

The Sum= 0
The Sum= 10
The Sum= 30
The Sum= 100
The Sum= 130

"""

# 3. Wap to check whether the given int is a multiple of 5 and 8

# What is the operator and define python logical operator?

# and  -> if both codition is true 
# or --> if atleast one condition is true
# not --> compliment 

# 5. In function how many types of variable is their described with examples?

# 4 types there :

"""
1. positional arg  --- 

def your_name(name,age):

  pass

your_name(age,name)


2. keyword arg :
3. default arg :
4. variable lenght arg :

"""

"""
Python oops : 29/03/22

"""



# def your_name(name,age):
#   print("hello",name,"your age",age)

# your_name(15,"adithi")

# TypeError: your_name() missing 2 required positional arguments: 'name' and 'age'

# hello adithi your age 15
# hello 15 your age adithi


"""
============
python class :
"""
# def fun():
#   pass


# class Adithi:
#   pass 

#   def fun():
#     pass


# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# class Student:
#   pass

#   ''' This is student class with required data '''


# print(Student.__doc__)
# help(Student)

# Example for class:


# # this is our class 
# class Student:
#   # this is constructor
#   def __init__(self):
#     self.name = input("Enter your name:")
#     self.age = int(input("Enter your name:"))
#     self.marks = int(input("Enter your name:"))

#   # this is method
#   def show(self):
#     print("Hello I am :",self.name)
#     print("My Age is:",self.age)
#     print("My Marks are:",self.marks)

# # input for taking data from user side

# # this is our object
# obj = Student()
# obj.show()

"""
output : 
Hello I am : adithi
My Age is: 40
My Marks are: 80
"""

"""
14/04/22
"""
"""
given all num/no of elements
 sum of num is = 28
 no of element is = 7

 avg = sum of num is / len(no of element is)

"""

# lists = [1,2,4,4,5,6,6]
# lists = eval(input("Enter int no with any sep:"))
# sum = 0
# for i in lists:
#   sum = sum+i

# avg = sum/len(lists)
# print("sum of all given no is:",sum)
# print("avg of all given no is:",avg)
# print("no of all given element is:",len(lists))

# sum of all given no is: 28
# avg of all given no is: 4.0
# no of all given element is: 7

"""

Welcome to  Deepti Bank
Enter your Name:deepti
d-Deposit 
w-Withdraw 
e-exit
Choose your option:1000
Invalid option..Plz choose valid option
d-Deposit 
w-Withdraw 
e-exit
Choose your option:d
Enter amount for deposit:1000
Balance after deposit: 1000.0
d-Deposit 
w-Withdraw 
e-exit
Choose your option:d
Enter amount for deposit:500
Balance after deposit: 1500.0
d-Deposit 
w-Withdraw 
e-exit
Choose your option:w
Enter amount for Withdraw:2000
Insufficient Funds..cannot perform this operation
"""








