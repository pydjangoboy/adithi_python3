"""
1.Write a program to print first 10 even numbers in reverse order.

2.Write a program to print table of a number accepted from user.

3.Accept 10 numbers from the user and display their average.

4.Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

 5.Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

6. How many times the following loop execute?
c = 0

while c < 20:

      c += 2
"""


# 1.Write a program to print first 10 even numbers in reverse order.
# 2,4,6,8,10 ==>10,8,6,4,2

# num  = range(0,11,2)
# print(list(num[::-1]))

# output :
# [10, 8, 6, 4, 2, 0]


# 2.Write a program to print table of a number accepted from user.
# hint : 1*2=2, 2*2 = 4 , 2*3=6 ....n

# num = int(input("Enter any int no:"))
# endvalue = int(input("Enter your end range:"))
# for i in range(1,endvalue+1):
#     print(i*num,end=" ")

# output
# 5 10 15 20 25 30 35 40 45 50


# 3.Accept 10 numbers from the user and display their average.
# 1,2,2,4,4,5,6,7,7,8,9,10
# num = eval(input("Enter any int from 1 to 10:"))
# sum = 0 
# for i in num:
#     sum = sum+i

# avg = sum/len(num)
# print("sum is:",sum)
# print("avg is:",avg)

# 2nd way:
# for i in range(start,stop)

# num = int(input("Enter any int from 1 to 10:"))
# sum = 0 
# for i in range(1,num+1):
#     sum = sum+i

# avg = sum/num
# print("sum is:",sum)
# print("avg is:",avg)
    

"""
4.Write a program to display sum of odd numbers and even numbers 
that fall between 12 and 37(including both numbers)
"""

# hint :given no is: 1,2,3,4,5,6,7,8,9,10
#         odd no is : 1,3,5,7,9
#        even no is:  2,4,6,8,10

# sum=0
# for i in range(12,38):
#     if i%2==0:
#         sum = sum+i
#         print("even no is:",i)
#         print("sum of all even no is:",sum)  
        
# print("===="*10)    

# sum1=0    
# for i in range(12,38):
#     if i%2!=0:
#         sum1 = sum1+i
#         print("odd no is:",i)
#         print("sum of all odd no is:",sum1)          

  
"""08/oct/21"""
# Eg: To print numbers from 1 to 10 by using while loop
# num=1
# while num<=10:
#     print(num,end=" ")
#     num = num+1       

 
# 2 . Write a program to print odd and even no using while loop
# num = int(input("Enter any int no:"))
# num1 = 1
# while num1<=num: # while 1 <= 10:
#     if num1%2==0:
#         print(num1)
#     num1 = num1+1    

# print a sqr of any no :

# print(num**2)    
# print(num*num) 

# num = int(input("Enter any int no:"))  
# t = 1

# while t <= num:
#     print(num,"*",t, "=",num*t)
    
#     t = t+1    
    
"""
Enter any int no:10
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100
"""    

"""13/Oct/21"""

""" infinite loop """

# using ctrl+c 

# i = 1
# while i>=0:
#     print("infinte loop",i)
#     i = i+1


# Transfer statements : break ,continue, pass

# 1. Break : 

# eg 1. 
# for i in range(11):
#     if i >= 7:
#         print("processing is enough..plz break")
#         break   
#     print(i)
        
        
# eg 2 .
# name = input("Enter your name :")
# age = int(input("Enter your age:"))

# for i in range(1,10):
#     if name == "adithi" and age == 10:
#         print("your name is :",name, "your age is:",age)
#         break
    
#     print(i)  


#2 . continue :   

# for i in range(1,20):
#     if i == 7:
#         continue
    
#     print(i,end=" ")

# output : 1 2 3 4 5 6 8 9 10 11 12 13 14 15 16 17 18 19

# 3. pass : just pass / nothing 

# i=10
# if i==10:
#     pass

# for i in range(1,200):
#     pass

"""Homework

1. To print odd numbers in the range 0 to 9 using countinue statement
2. How to exit from the loop?
3. How to skip some iterations inside loop with example?
4. When else part will be executed wrt loops with example?

5. Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

Given: -
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

Expected Output: -
[20, 60, 30]

"""   

""" 20/OCT/21"""

# quesiton no : 1 : write a programm ot print 1 to 10 num and add all of them using while loop

# num = int(input("Enter any int no:")) # 10
# num1 = 1 
# sum = 0 

# while num1 <= num:     
#     print(num1) 
#     sum = sum+num1  
#     num1 = num1+1 
    
# print("sum of all no is :",sum)



# for i in range(1,20):
#     if i >= 14:  
#         break
    
#     print(i,end=" ")

# out : 1 2 3 4 5 6 7 8 9 10 11 12 13


#  eg 2  : # 3. How to skip some iterations inside loop with example? 

# for i in range(1,20):
#     if i == 14:
#        continue
   
#     print(i,end=" ")
  
# out :  1 2 3 4 5 6 7 8 9 10 11 12 13 15 16 17 18 19


"""Homework : 20/oct/21"""
# write a program to print if name is adithi or adi, deepti then skip the name and print other name : 




# 26/10/21

# write a program to print even no using continue statatments

# for i in range(1,200):
#     if i%2 == 0: 
#         continue 
#     print(i,end=" ")
        

# num = int(input("Enter any int no:"))
# num1 = 1


# list Comprehensions

# odd no using normal way :
# for i in range(1,200):
#     if i%2==0:
#         print(i,end=" ")
   

""" 
Syntax:
=========

var1 = [ expression for item in list if condition ] # list

var2 = ( expression for item in list if condition ) # tuple

  
"""

# odd no using list Comprehensions :

#  squar of any int no

# s = [ i**2 for i in range(1,11)]
# print(s)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 


# # even no using list Comprehensions :
# s = [ i for i in range(1,200) if i%2==0 ]
# print(s)

"""
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80,
82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118,
120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154,
156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 
192, 194, 196, 198 ]
"""

""" 29/OCTY/21"""

# odd no using tuple Comprehensions :
# s = (i for i in range(1,200) if i%2!=0  )
# for x in s:
#     print(x,end=" ")
        
# Set Comprehension:
# sc = { i for i in range(1,200) if i%2==0 }
# print(sc)
        
        
# dict Comprehension : 
# dict = {1:"one",2:"two"}

# squares = { x : x*x for x in range(1,6) }
# print(squares)

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#  odd and even no 
# odd_and_even = { i : i*2 for i in range(1,20) }
# print(odd_and_even)

# print(odd_and_even.keys())
# print(odd_and_even.values())

# for k,v in odd_and_even.items():
#     print("key is:",k ,"value is:",v)


# {2: 2, 4: 4, 6: 6, 8: 8, 10: 10, 12: 12, 14: 14, 16: 16, 18: 18}
# dict_keys([2, 4, 6, 8, 10, 12, 14, 16, 18])
# dict_values([2, 4, 6, 8, 10, 12, 14, 16, 18])

   
# tc = (i for i in range(1,20))    
# print(tc)    
# <generator object <genexpr> at 0x7fb9c145d9e0>

# for i in tc:
#     print(i,end=" ")
    
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19    

# 3/Nov/21

# list comp
# odd_even = [ f"{i} even no" if i%2==0  else f"{i} odd no" for i in range(20)]
# print(odd_even)

# for i in odd_even:
#     print(i)
    
    
# a,b,c,d = 10,20,30,40
# # print(b,c,a,d)   

# print("a for apple {}, b for boy{}, c for cat{}, d for doll{}".format(a,c,b,d))

# # a for apple 10, b for boy20, c for cat40, d for doll30


# homework : 
"""
1. Create a list from the elements of a range from 1200 to 2000 with steps of 130, 
using list comprehension.
2 .Use list comprehension to construct a new list but add 6 to each item.
3. Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
4. Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.
5. First, create a range from 100 to 160 with steps of 10.
Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.
"""

"""Nov/10/21"""

"""
s='This is ' single quote symbol' ==>invalid
s='This is \' single quote symbol' ==>valid
s="This is ' single quote symbol"====>valid
s='This is " double quotes symbol' ==>valid
s='The "Python Notes" by 'durga' is very helpful' ==>invalid
s="The "Python Notes" by 'durga' is very helpful"==>invalid
s='The \"Python Notes\" by \'durga\' is very helpful' ==>valid
s='''The "Python Notes" by 'durga' is very helpful''' ==>valid
"""

# s1 = 'this is that"s single quote'
# s2 = 'this is that\'s single quote'
# print(s1)
# print(s2)
# this is that"s single quote
# this is that's single quote

# 1. THIS IS SINGLE QUOTE SYMBOL --->upper case
# 2. This Is Single Quote Symbol --->title case

# s="This is single quote symbol" 
# print(s.upper())
# print(s.title())
# print(s.lower())

"""
Eg:
 
1. isalnum(): 
Returns True if all characters are alphanumeric( a to z , A to Z ,0 to 9 )
eg : thisThis01 
 
isalpha(): 
Returns True if all characters are only alphabet symbols(a to z,A to Z)
eg : thisThis

isdigit(): 
Returns True if all characters are digits only( 0 to 9)
eg : 0 - 9 --->,1,2,3,4,5,6,7

islower(): 
Returns True if all characters are lower case alphabet symbols
eg : this

isupper(): 
Returns True if all characters are upper case aplhabet symbols
eg: uppercase

istitle(): 
Returns True if string is in title case
eg : This Is Word 

isspace(): 
Returns True if string contains only spaces
eg : "        " 
"""
# Homework : 
""" 1. Read:
============ 
1. what is funtions and how to define and which keyworkd is required for defining
2. types of funtions 
3. revise control flow statements and list Comprehensions,tuple Comprehensions,
dict Comprehensions.
"""


# 26/11/2021

#Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
# x=[i for i in range(1200,2000,130)] 
# print(x)

#?Write a programm to print 1 to 10 num and sum all of them using while loop
# 1,2,3,4,5,6,7,8,9,10 ===> 

# sum = 0
# num = 1
# while num <= 10:
#     sum = sum + num
#     print(sum)
#     num = num +1

#3 ?First, create a range from 100 to 160 with steps of 10.Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value.

# x={i:i/100 for i in range(100,160,10)}
# print(x)




