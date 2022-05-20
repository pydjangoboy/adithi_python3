
"""01/Sep/21 class example
============================
"""

"""
num = int(input("Enter any type of input like list,tupel,set,float:"))
print(num)

num = eval(input("Enter any type of input like list,tupel,set,float:"))
print(num)

"""

# q.2 :  avg of 5 numbers 
""" 
1 step :      1,2,3,4,5 ===> 1+2+3+4+5 = 15
2 nd step :   sum of all num / no of elements 
3rd step :    avg =  15/5 = 3
"""

num = eval(input("Enter 5 elements/numbers :"))
sum = 0

for i in num:
  sum = sum+i 
  
avg = sum / len(num)

print("sum of all num is:",sum)
print("Avg for all elements is:",avg)

"""output :
Enter 5 elements/numbers :[1,2,3,4,5]
sum of all num is: 15
Avg for all elements is: 3.0
"""

# 3. write a program to check username ,password, age, phone_no using if statements:
username = input("Enter your name :")
password = input("Enter your password:")
age = int(input("Enter your age:"))
phone_no = int(input("Enter your phone_no:"))

if username == "adithi" and password == "adithi123@" and age == 15 and phone_no == "+912345":
  print("Hlo user your :",username,"and your age is:",age,"your cell phone no is:",phone_no) 
else:
  print("Your input is invalid try again")

"""
output : 
========

Enter your name :adithi
Enter your password:adithi123@
Enter your age:15
Enter your phone_no:+9123  
Your input is invalid try again

"""

# Assignment operator : = , += ,-=

a = 10
a += a # a = a+a
print(a)

b = 10
b -= b # b = b-b
print(b)


"""
Assignment Operators:
====================
We can use assignment operator to assign value to the variable.
Eg: x=10

 We can combine asignment operator with some other operator to form compound
 assignment operator.
 Eg: x+=10 ====> x = x+10
 The following is the list of all possible compound assignment operators in Python
+= 
-=
*=
/=
%=
//= 
**=
&=
|=
^=
>>=
<<=
"""
# # Eg:
x=10
x+=20
print(x) #30

""" Homework is :
Practice :
===========
1.  Average no program
2. and ,or , not operator 
3. eval functions
4. assingnement operator 
"""

num1,num2 = input("Enter two no:").format(",")
x = print("num1 is greater than num2")  if num1>num2 else print("num1 is lessthan num2")

