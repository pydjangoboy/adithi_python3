'''List'''

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
# l = [1,5,6,6,8,9,5,44,9]
# print(l) # [1, 5, 6, 6, 8, 9, 5, 44, 9]
# l.sort()
# print(l) # [1, 5, 5, 6, 6, 8, 9, 9, 44]


# basic opeartion of list :
# type(), how to access=> indexing, insert(),pop(),remove(),sort()


''' Home work based on List '''

"""
Question based on string slicing and list data types: 
1. What is the output of the following code?
sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

2. What is the output of the following code
aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])    
print(aList[1][3])

3. What is the output of the following list operation
sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

4. What is the output of the following list operation
aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

5. What is the output of the following list assignment
aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)
[4, 20, 24, 28, 8, 12, 16]
[4, 20, 24, 28]

6. What is the output of the following list function?
sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

7. What is the output of the following
aList = [5, 10, 15, 25]
print(aList[::-2])
[15, 10, 5]
[10, 5]
[25, 10]

# Question based on data types

1. What is the output of the following code
print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
2. What is the data type of the following
aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))

3. What is the data type of :
print(type(10))
print(type(10.5))
print(type(10+2j))

4. What is the result of print(type([]) is list)

5. What is the output of the following code?
valueOne = 5 ** 2
valueTwo = 5 ** 3

print(valueOne)
print(valueTwo)

6. What is the output of the following
x = 36 / 4 * (3 +  2) * 4 + 2
print(x)

7. What is the output of the following code?
for i in range(10, 15, 1):
  print( i, end=', ')


"""

"""Aug/06/21"""
# Creation of List Objects:

# 1. We can create empty list object as follows :


# 2. If we know elements already then we can create list as follows :


# 3. With dynamic input:


# 4. With list() function:


# note :
# Sometimes we can take list inside another list,such type of lists are called 
# nested lists. ==> [10,20,[30,40]]


l = [1,2,3,4,5]
print(l[::-1])





