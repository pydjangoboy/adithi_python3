print("==========================23/july/2021=======================")

# 23/july/2021 : class examples

'''
class example :
1. identifiers
2. how many python inbuilt keyword is their ? 
and how to print python inbuilt keywords ?
3. python data types 
4. imp command for checking python version and how to run python file on terminal
5. basic commands

'''
'''
# 1. identifier :

name = "this is our var name"
import keyword # this is our module
# def name ==> function name
# class name ===> class name

def adithi(var1,var2):
    pass

class adithi(var1,var2):
    pass
    
'''

'''
# on python idle  :
>>> 10 
10
>>> "this is string"
"this is string"
'''

# note : on idel print is not Required for printing values
#        but any code editor print is required for printing values

# import keyword  # this is moudle/lib
# print(keyword.kwlist)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
'raise', 'return', 'try', 'while', 'with', 'yield']
'''

# data types :
# 11 + python inbuilt data types

# int=10,
# float = 10.0
# bool = True,False
# name = "this is string/char"
# com = 10+2j # 10 is real part and 2j is imag part
# # complex give float value
# print(com)
# print(com.real)
# print(com.imag)
# output : 
# 10.0
# 2.0

# imp data types:

# list,tuple,set,dict,

# list and operations with indexing:

# l = ["this is str", 1 ,True,10+2j,10.5,5]
# 0, 1, 2, 3, 4 ,5 ==> this is id of your list value

# output :
#['this is str', 1, True, (10+2j), 10.5]  

# indexing how to access list value
# print(l) #['this is str', 1, True, (10+2j), 10.5, 5]
# print(l[3]) #(10+2j)
# print(l[5]) #5

# # how to insert value inside list :
# l.insert(6,"new") # insert take two parameters  : 6 is index and "new" is value
# print(l) #['this is str', 1, True, (10+2j), 10.5, 5, 'new']


# what we did :
# data types , int,float,bool,str,complex (how to access real and imag value)
# list  == > how to access list value and how to insert new value
# indexing how it's works



# home work : 23/07/21 :  
# 1. how to check python version using command promt ==>python --version,py -V,py --version
# 2. how to move into one dir to other using command promt ==> cd 
# 3. how ot run python program using command promt ==>python3 test.py, python test.py
# 4. what is identifier and how to define ==>a=10,b ="this",c=10.5
''' 
5. pratice on your sublime and save with output :
identifiers,data types,
list operations ==> indexing ,how to access value, how to insert new value 
'''

print("=========================================")


# list :
# l = [1,"this",2,10.05,True,10+2j]
# #    0,1,2,      3,    4,   5

# print(l)
# print(type(l))

# output:
# [1, 2, 'this', 10.05, True, (10+2j)]
# <class 'list'>

# how to access list of value using indexing :
# print(l[2]) # this

# how to insert new value into list :
# l.insert(6,"new")
# print(l) #[1, 2, 'this', 10.05, True, (10+2j), 'new']

# how to remove :
# 1,2,2,3,4,5  == start =1,  end =5 ==> remove last value 
# from list

# l.remove("new")
# print(l) #[1, 2, 'this', 10.05, True, (10+2j)]

# how remove last value using pop functions :
# l.pop(5)
# print(l) #[1, 2, 'this', 10.05, True]

# l.pop()
# print(l) 
# [1, 2, 'this', 10.05]

# l.pop()
# print(l) 
# # [1, 2, 'this']

# sort your value which is present in l
l = [1,5,6,6,8,9,5,44,9]
# print(l) # [1, 5, 6, 6, 8, 9, 5, 44, 9]
# l.sort()
# print(l) # [1, 5, 5, 6, 6, 8, 9, 9, 44]


# basic opeartion of list :
# type(), how to access=> indexing, insert(),pop(),remove(),sort()


l.insert()

