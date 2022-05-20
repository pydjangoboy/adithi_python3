
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

def sum_of_even_no(lists):
    sum = 0
    for i in lists:
        if i%2 == 0: # for odd ---> if i%2 != 0:
            # sum of all even no which div by 2
            sum = sum + i
    print("Sum of even no is:",sum)


# lists = [1,2,3,4,5,6,7,8] # 2,4,6,8 = 20
# sum_of_even_no(lists)
# Sum of even no is: 20

lists = range(1,5) # 1,2,3,4
sum_of_even_no(lists)

# homework : 
"""
Q1. Write a function to find factorial of given number?
input : 5 
output : 5*4*3*2*1 = 120

Q2. Write a function to display the given integer in reverse manner 
input : 567
output : 765

Q3. Write a function to find the sum of the digits of an integer using while loop

"""
    

