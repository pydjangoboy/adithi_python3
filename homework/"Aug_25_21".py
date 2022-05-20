"""
class example and homework: 
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

"""homework """

"""
Q.1. Program for minimum of 3 numbers
Q.2. Program for maximum of 3 numbers
Q.3. Write a program to read 2 numbers from the keyboard and print sum.

output test cases :

Output: for question 1
 D:\python_classes>py test.py
 Enter First Number:10
 Enter Second Number:10
 Both numbers are equal
 
Output: for question 2
 D:\python_classes>py test.py
 Enter First Number:10
 Enter Second Number:20
 First Number is Less than Second Number
 
 """

