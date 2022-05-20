  
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

num = int(input("Enter any int no:"))  
t = 1

while t <= num:
    print(num,"*",t, "=",num*t)
    
    t = t+1    
    
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


"""Homework"""
"""
1 .Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".


2. Write an infinite loop.
A inifinte loop never ends. Condition is always true.

"""



