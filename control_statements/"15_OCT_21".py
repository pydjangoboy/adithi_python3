
# quesiton no : 1 : write a programm ot print 1 to 10 num and add all of them using while loop

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

        