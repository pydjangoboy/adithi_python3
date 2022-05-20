
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


""" homework """

# 1. write a program to print odd and even nd zero no using list Comprehension

# 2. write a program to print odd and even nd zero no using tuple Comprehension

# 3. write a program to print odd and even nd zero no using dict Comprehension

# 4. write a program to print odd and even nd zero no using set Comprehension

