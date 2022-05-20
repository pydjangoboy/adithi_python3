
# b = (72/9*(10-2+5)*20+2-5) # 2077 
# print(b)

# a = 36/4*(3+2)*4+2
# print(a)
#   36/4* (5)*4+2
#    9  *  5 *4+2
#      45    *4+2
#      45*4=180+2
#            182

# () / * ,** +,-

# b = (72/9*(10-2+5)*20+2-5) # 2077 
# print(b)
#      8 *   13   *20

'''
1. The ASCII value for a is 97 and for z is 122. Therefore, 
looping over every integer between the range returns the alphabets from a-z.
==>a to z == 97 to 122 for small char

2. ASCII value for capital A is 65 and for capital Z 90.
==>A to Z == 65 to 90 for small char 
total char of alphabat is  : 25

3.ASCII codes represent text in computers, 
telecommunications equipment, and other devices.
'''

# 1. i want to print (a to z) in lower case

# for i in range(97,122+1):
#     print(chr(i),end=' ')

# a b c d e f g h i j k l m n o p q r s t u v w x y z % 

# 1. i want to print (A to Z) in upper case == A B C ...Z
# for i in range(65,90+1):
#     print(chr(i),end=" : ")
     
# for upper case 65 to 90
# for lower case 97 to 122

#  some imp fun for list or tuple or set
"""
1. len() ==> return the number of element preset in variable
2. count() ==> it return the number of occurrences of specified item in the variable

"""
# for len()
# v = [1,2,3,4,5,56,7,7,7,7,5,5,5]  # 5->4, 7->4
# print(len(v)) # 8

# # for count()
# print(v.count(7)) #4

'''Set data types'''
# s = {9,6,5,3,True,6,7,4,3,10+2j}
# print(s)

# {True, 3, 4, 5, 6, 7, 9, (10+2j)}
# {1, 2, 3, 4, 5, 6, 7, 9}

# s2 = set(range(1,20,2))
# print(s2)
# print(type(s2))

# {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
# <class 'set'>

# s2 = list(range(1,20,2))
# print(s2)
# print(type(s2))

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# <class 'list'>

# for printing three digit random number

# from random import *
# for i in range(randint(111,222),randint(111,222),randint(111,222)):
#     print(i,end=' ')


"""Homewrok aug/11/21"""
"""
Python set data types homework 13/05/21
=======================================

1. What is the output of the following set operation
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set3 = set2.difference(set1)
print(set3)

2. What is the output of the following
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Blue")
print(sampleSet)

3. What is the output of the following union operation
set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}

set3 = set1.union(set2)
print(set3)

4. The union() method returns a new set with all items from both sets by removing duplicates
	•	True
	•	False

5. What is the output of the following
	•	sampleSet = {"Yellow", "Orange", "Black"}
	•	sampleSet.add("Blue")
	•	sampleSet.add("Orange")
	•	print(sampleSet)

6. What is the output of the following code
sampleSet = {"Yellow", "Orange", "Black"}
print(sampleSet[1])

7. What is the output of the following code
aSet = {1, 'PYnative', ('abc', 'xyz'), True}
print(aSet)

8. What is the output of the following set operation
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.update(["Blue", "Green", "Red"])
print(sampleSet)


"""