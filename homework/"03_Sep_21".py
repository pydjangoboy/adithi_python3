""" 02/Sep/21  class example and homework"""

# Assignment operator : = , += ,-=

a = 10 # assigning value
a += a # a = a+a  ==> # increasing value with one
print(a)

a = 10 # assigning value
a = a+10 # a = a+a  ==> # increasing value with one
print(a)

b = 10
b -= b # b = b-b
print(b)

# Ternary operator :

# normal way 
num1 = int(input("Enter no 1:"))
num2 = int(input("Enter no 2:"))

if num1 > num2:
  print("Num1 is greater")
else:
  print("num1 is lessthan of num2")  
  
# ternary operator : program for lessthan or greater than

num1,num2 = [ int(i) for i in input("Enter two no:").split(":")]
print("num1 is greater") if num1>num2 else print("num1 is lessthan of num2")  

"""Homework"""  

"""
1. What is the output of print('[%c]' % 65)
2.Given a list of numbers, Iterate it and print only those numbers which are divisible of 5 
3.Given two integer numbers return their product. 
    If the product is greater than 1000, then return their sum

def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)
  
    
sample input and output :
=========================

Given 1:

number1 = 20
number2 = 30
Expected Output: The result is 600


Given 2:

number1 = 40
number2 = 30
Expected Output: The result is 70


"""