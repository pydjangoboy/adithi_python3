"""
1.Write a program to print first 10 even numbers in reverse order.

2.Write a program to print table of a number accepted from user.

3.Accept 10 numbers from the user and display their average.

4.Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

 5.Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

6. How many times the following loop execute?
c = 0

while c < 20:

      c += 2
"""

"""
# 1.Write a program to print first 10 even numbers in reverse order.
# 2,4,6,8,10 ==>10,8,6,4,2

num  = range(0,11,2)
print(list(num[::-1]))

# output :
# [10, 8, 6, 4, 2, 0]


# 2.Write a program to print table of a number accepted from user.
# hint : 1*2=2, 2*2 = 4 , 2*3=6 ....n

num = int(input("Enter any int no:"))
endvalue = int(input("Enter your end range:"))
for i in range(1,endvalue+1):
    print(i*num,end=" ")

# output
# 5 10 15 20 25 30 35 40 45 50


# 3.Accept 10 numbers from the user and display their average.
# 1,2,2,4,4,5,6,7,7,8,9,10
num = eval(input("Enter any int from 1 to 10:"))
sum = 0 
for i in num:
    sum = sum+i

avg = sum/len(num)
print("sum is:",sum)
print("avg is:",avg)

# 2nd way:
# for i in range(start,stop)

num = int(input("Enter any int from 1 to 10:"))
sum = 0 
for i in range(1,num+1):
    sum = sum+i

avg = sum/num
print("sum is:",sum)
print("avg is:",avg)
    

# 4.Write a program to display sum of odd numbers and even numbers 
# that fall between 12 and 37(including both numbers)


# hint :given no is: 1,2,3,4,5,6,7,8,9,10
#         odd no is : 1,3,5,7,9
#        even no is:  2,4,6,8,10

sum=0
for i in range(12,38):
    if i%2==0:
        sum = sum+i
        print("even no is:",i)
        print("sum of all even no is:",sum)  
        
print("===="*10)    

sum1=0    
for i in range(12,38):
    if i%2!=0:
        sum1 = sum1+i
        print("odd no is:",i)
        print("sum of all odd no is:",sum1)       
            
"""
    
"""HOEMWORK 06/OCT/10"""

"""
1. Write a program to print all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5.

2 . Write a program to print odd and even no using while loop

3 . Write a program to print odd and even no using while loop

4 .Write a program to print table of a number accepted from user , using while loop
"""    