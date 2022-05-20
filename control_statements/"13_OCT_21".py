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


"""Homework 13/oct/21 :

1. To print odd numbers in the range 0 to 9 using countinue statement
2. How to exit from the loop with example?
3. How to skip some iterations inside loop with example?
4. When else part will be executed wrt loops with example?

5. Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

Given: -
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

Expected Output: -
[20, 60, 30]

"""   

# quesiton no : 1 : write a programm ot print 1 to 10 num and sum all of them using while loop

num = int(input("Enter any int no:")) # 10
num1 = 1 # 2
sum = 0 # 1

while num1 <= num: 
    # 1 <= 10 ---> True ,
    # 2 <= 10 ---> True,
    
    print(num1) 
    # 1,2,

    sum = sum+num1 
    # sum = 0+1 ==> 1
    # sum = 1 + 2 ==>  sum = 3
    
    num1 = num1+1 
    # num1 = 1+1 = 2
    # num1 = 2+1 ==> num1 ==> 3
    
print("sum of all no is :",sum) 

        