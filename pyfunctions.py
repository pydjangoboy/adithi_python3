# 26/11/21

# function : is collection of var ,class 
# 
#  two of functions is there : 

# 1: inbuilt function  ==> print(), id(), input()
# print("this is inbuilt funtions",end=" ")

# 2: user define function ==> 
# i want to make one calculator for arithmetic operations:

# note : 1. defining fun u have use def , 2. put ur function name in small case

# def cal_operations(a,b):
#     sum = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     mud = a%b
#     print(sum,sub,mul,div,mud,sep="\n")

# cal_operations(10,20)    

# out  : 

"""
30
-10
200
0.5
10
"""

#write a program to print avg of 10 num using functions: 

# def avg(num):
#     pass
    
    

# num = eval(input("Enter 10 no with any sep like :"))
# avg(num)

# 1. Built in Functions: print(),type(),id()
# 2. user define functions :

# def ap():
#     a = 20+30
#     b = 20-30
#     print(a,b)

# ap()  #50 -10 

# TASK : 1  write a program to print avg of 5 num using functions:

# 1st way for 5 no of avg : 
# def avg(avglist):
#     sum = 0
#     for i in range(avglist):
#         sum = sum+i
#         avg = sum/len(avglist)
#         print("Avg of all given no is:",avg)

# avglist=eval(input("Enter your list:"))
# avg(avglist)

# 2nd way for 2 no of avg :

# def avg_of_two_no(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print("avg of two no is:",avg)

# avg_of_two_no(10,20,100)

# avg of two no is: 20.0

# task 2 no : 



# 03/11/21

"""list = [1,2,3,4,"this",10.5,True,10+2j]
list = []

n1 = 1,2,3,4,5,5
num = list(n1)
"""


# tp = 1,2,3,4
# print(type(tp))

# tp = ()
# print(type(tp))

# tp = 1,2
# print(type(tp))

# tuple = (1,2,3,4,4,5,6,6,"this is tuple")
# dict = {1:"adi", 2:"rishan", 1:"one"}
# print(dict)
# note : 1 is key, adi is value,  2 is key and rishan is a value
# print(type(dict))


# s = {1,2,3,4,2,22,2,2,23,3,3}
# print(s)
# print(type(s))

"""{1, 2, 3, 4, 22, 23}
<class 'set'>"""


# task is  : control statements : if,if-else, if-elif, for, while,break continue,pass

""" wed/08/21"""

# num = eval(input("Enter any int no:"))
# sum=0
# for i in num:
#     sum = sum+i
#     avg = sum/len(num)

# print("No of given input no is:",len(num))   
# print("Sum of all given no is:",sum)
# print("Avg of all given no is:",avg)

"""output:
Enter any int no:1,2,3,4,5,6,3,2 
No of given input no is: 8
Sum of all given no is: 26
Avg of all given no is: 3.25"""

# def avg_num(num):
#     sum=0
#     for i in num:
#         sum=sum+i
#         avg=sum/len(num)

#     print("No of given input no is:",len(num))
#     print("Sum of all given no is:",sum)    
#     print("Avg of all given no is:",avg)    

# num = eval(input("Enter your int input for avg:"))
# avg_num(num)

# parameters : 
"""write a function to take name of the student as a input and print wish message by name"""
# 1.case:
# def wish(name):
#     print("name of student is :",name)

# wish("adithi") # name of student is : adithi

# 2. case: 
# def student_details(name,age,locations,phoneno):
#     print("Studnet name is:",name)
#     print("Studnet age is:",age)
#     print("Locations is :",locations)
#     print("Phone no of student is:",phoneno)

# student_details("Adithi",10,"USA",+9120032323)

"""
Studnet name is: Adithi
Studnet age is: 10
Locations is : USA
Phone no of student is: 9120032323
"""

"""squar of no 
2 is 2*2 = 4
4 is 4*4 = 16
3 is 3*3 = 9
"""


# 15/12/21 

# pass with funtions : 
# def sum(num):
#     if num%2 == 0:
#         print("num is even")
#     else:
#         pass # nothing just pass 35/100 u just pass

# num = int(input("Enter your input:"))
# sum(num)

"""
Task : using funtions :

if no is div/2 nd rem is 0 then given input is even
if it is not then odd

i want to take input num from user side
"""
# while True :
#     # whole logic is inside of while loop
#     def even_odd(listname):
#         if listname%2 == 0:
#             print(listname,"no is even") # inside if statements
#         else: # this is inside of funtion
#             print(listname,"no is odd") # this is inside of else   

#     # out of the functions
#     listname = int(input("Enter any int no:"))
#     even_odd(listname)

# """
# Enter any int no:55
# 55 no is odd
# """

"""
Task : 2 : using funtions : 

if no is even then sum of all given no (only sum of all even no)
 like : 2,4,6,8,3,6,7,3,5,3,10 ===> 2,4,6,8,6,10
"""

# import random 
# print(random.randint(1,10))

# 2,4,6 = sum = 12

# def sum_of_even_no(lists):
#     sum = 0
#     for i in lists:
#         if i%2 == 0: # for odd ---> if i%2 != 0:
#             # sum of all even no which div by 2
#             sum = sum + i
#     print("Sum of even no is:",sum)


# lists = [1,2,3,4,5,6,7,8] # 2,4,6,8 = 20
# sum_of_even_no(lists)
# Sum of even no is: 20

# lists = range(1,5) # 1,2,3,4
# sum_of_even_no(lists)

# homework : 
"""
Q1. Write a function to find factorial of given number?
input : 5 
output : 5*4*3*2*1 = 120

Q2. Write a function to display the given integer in reverse manner 
input : 567
output : 765

Q3. Write a function to find the sum of the digits of an integer using while loop
123 = 6
"""
    
# 3 task : 

# def sum_of_all_digits(num):
#     sum=0 # 0 | 3 | 5 | 6 
#     while num > 0 : # 123 > 0 | 12 > 0 | 1>0  | 0 > 0 ----> condition becomes false
#         rem = num%10 # rem = 123%10 = 3 | rem = 12%10 = 2 | rem = 1%10 = 1 
#         sum = sum+rem # sum = 0+3 = 3 | sum = 3+2 = 5 | sum = 5+1= 6
#         num = num//10 # num = 123//10 = 12 | 12//10 = 1 | num = 1//10 = 0
#     print("sum of all digit is:",sum) #  3 | 5 | 6

# num = int(input("Enter any int no :")) # 123
# sum_of_all_digits(num)

"""
11234 = 11 total
note : 
modulo = give rem
floor div = depened on input if input is int then output will be int
            if input is float then output will be float

"""

"""
Q1. Write a function to find factorial of given number?
input : 5 
output : 5*4*3*2*1 = 120

5! = 5*4*3*2*1 = 120
0! = 1
1! = 1

neg no is not working
"""
# 1st way:

# import math 
# def factorial_no(num):
#     fact = math.factorial(num)
#     print(fact)

# num = int(input("Enter any int no:"))
# factorial_no(num)
    
# 2nd way : 
# def fact(num):
#     fact = 1 
#     i = 1 
#     while i <= num: 
#         fact = fact*i 
#         i = i+1 
#     print("Factorial of given no is:",fact)        

# num=int(input("Ennter any int no:"))
# fact(num)

"""
Ennter any int no:5
Factorial of given no is: 120

Ennter any int no:1
Factorial of given no is: 1
"""


# for loop : 
# using for loop to print 1 to 10 int num

# for i in range(1,11):
#     print(i,end=" ") 
# 1 2 3 4 5 6 7 8 9 10    

# while loop :
# using while loop to print 1 to 10 int num
# i=1 # 2 | 3
# while i <= 10: # 1 <= 10 --> True | 2 <= 10-->True
#     print(i,end=" ") #1,2
#     i=i+1 # i = 1+1 = 2 | i = 2+1 =3

# 1 2 3 4 5 6 7 8 9 10    

"""
>>> num=2
>>> print(num*2)
4
>>> print(num = num+4)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(num = num+4)
TypeError: 'num' is an invalid keyword argument for print()
>>> num+4
6
>>> num += 4
>>> print(num)
6
>>> num -= 4
>>> print(num)
2
>>> num=num-4
>>> print(num)
-2
>>> n=12
>>> print(n*20)
240
>>> print(n**2)
144
"""

# 5/jan/22 
# for loop : 1 to 10 int 
# for i in range(1,11):
#   print(i,end=" ")

# while loop:

# i = 1
# while i<=10:
#   print(i,end=" ")
#   i = i+1 # i += 1

# what is factorial : 
"""
factorial, in mathematics, the product of all positive integers less than or equal to a given positive integer and denoted by that integer and an exclamation point. Thus, 
factorial seven is written 7!, meaning 1 × 2 × 3 × 4 × 5 × 6 × 7. 
Factorial zero is defined as equal to 1.
"""

""" task :
Q2. Write a function to display the given integer in reverse manner/order
input : 567
output : 765
"""
# 09/jan/22

# %  --> rem
# //  --> qut 
"""
requirend things :
if u entered any int 78998889 ---> input fun is required
condition is required
"""

# def rev_num(num):
#   reverse = 0 # | 7 | 76 | 7 6 5
#   while num > 0: # 567 > 0 --> True | 56 > 0 : True | 5 > 0 : True | 0 > 0 : False
#     digit = num%10 # digit =  567%10 = 7 | 56%10 = 6 | 5%10 = 5
#     reverse = reverse*10+digit # reverse = 0*10+7 = 7 | 7*10+6 =  76 | 76 *10 + 5 = 765
#     num = num//10 # num = 567//10 = 56 |  56 //10 = 5 | 5 // 10 = 0
#   print("Reverse of the number is:",reverse) # 765 

# num = int(input("Enter any int num:")) # 567
# rev_num(num)




# 17/01/22

# Task : using for loop

# def rev_num(num):
#   reverse = 0 

#   # while statements
#   # while num > 0: 
#   #   digit = num%10 
#   #   reverse = reverse*10+digit 
#   #   num = num//10 

#   # for statements :
#   for i in range(1,num):
#     if num > 0: 
#       digit = num%10
#       reverse = reverse*10+digit
#       num = num//10

#   print("Reverse of the number is:",reverse) 

# num = int(input("Enter any int num:")) 
# rev_num(num)

# for i in range(1,10+1):
#   print(i,end=" ")

# note : 
"""
for loop:
========
1.if we know the range like (i want to print 1 to 100 num ) then we should go for for loop

2. sepcific range ---> (1,2200)

3. no increment requirement is required

while loop:
===========

1.if we  don't know the range then we should go for while loop
like this

2. one variable is also required 
3. increment is required

num = 0
while  num<10:
  print(num,end=" ")
  num = num +1


==========
functions:
==========
1. while ur writing any program with function 
  a. define function with any name with any parameter
    like --> def name(num):
                print("hllo",num)
             num = int(input("enter any int no:")) 
             name(num) 

2. after logic u have to call ur functions with functions name
3. if any input ur taking then u have to write after the logic (out side of the function)
4. u have to call ur function outside of the functions block with functions name 

"""


"""
for test : 
==========
1. prepare control statements 
2. functions
3. most imp ---> a. for loop , b. while loop
4. try to write a single programm atleast 3 way like :
    a. using while loop
    b. using for loop
    c. using python inbuilt functions
5. revise how to print a to z lower case and upper case
"""

"""
1.
*
**
***
****
*****
"""
# for row in range(1,6):
#   for col in range(1,row+1):
#     print("*",end=" ")
#   print() # for printing blank line  


"""

24/03/22
"""

"""



3. Wap to check whether the given int is a multiple of 5 and 8
What is the operator and define python logical operator?

4. What is a while loop and give an example for that?

4. Write a program to print factorial of any int number using functions (with for loop)


5. In function how many types of variable is their described with examples?

6. What is functions and types with examples?

7. What is if-else, if-elif-else, if elif-else statements? and write an example for all conditions.

8. What is a while loop and give an example for that?

9. Write a program to print 1 t 10 int number using a while loop.

"""






  

  
