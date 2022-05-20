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
ls = [1,2,3,4,5]
sum=0
for x in ls: 
  sum = sum+x 
  # sum = 0+1 = 1, sum = 1+2 = 3, sum = 3+3=6, sum = 6+4 = 10, sum = 10+5 = 15
  print("sum of list is:",sum)
  
"""
sum of list is: 1
sum of list is: 3
sum of list is: 6
sum of list is: 10
sum of list is: 15
"""  