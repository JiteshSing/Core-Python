#####Q1############

'''num1 = int(input("Enter a first number "))
num2 = int(input("Enter a  second number "))

if num1>num2:
    print(num1,"is maximum")
else:
    print(f"{num2} is maximum")'''

#######Q2############
'''num1 = int(input("Enter a first number "))
num2 = int(input("Enter a  second number "))
if num1>num2:
    print(num2,"is minimum")
else:
    print(f"{num1} is minimum")'''

#######Q4###########
'''num = int(input("Enter a number "))
a=1
for i in range(1,num+1):
    a= a * i

print("Factorial of ", num, " = ", a)'''

######Q6##########
'''num = int(input("Enter a number "))
a=0
b=1
c=0
for i in range(1,num+1):
    print("Fibonacci series : ",c)
    a = b
    b = c
    c = a+b'''
#######Q7#########
'''for i in range(100,200):
    if(i%7==0):
        print("It's divisible by 7 :",i)'''

######Q12#########
'''cha = input("Enter a character")
revpalin = ""
for i in cha:
    revpalin = i+revpalin

if(cha == revpalin):
    print("It's a palindrome")
else:
    print("It's not a palindrome")'''

#######Q11###########
'''num1 = int(input("Enter a number "))
a=0
for i in range(1, num1+1):
    if(num1%i==0):
        a +=1

if(a==2):
    print("It's a prime number")
else:
    print("It's not a prime number")'''
#########Q3############
'''from random import*
print(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))'''
########Q5###########
'''num = int(input("Enter a number greater single digit "))
strn = str(num)
rev = ""
for i in strn:
    rev = i + rev

reve =int(rev)
if(num == reve):
    print("It's a reverse number")
else:
    print("It's not a reverse number")
'''

########################odd value in list#########
'''ele = [2, 3, 4, 5, 6, 7, 8]
for i in ele:
    if(i%2==1):
        print(i)'''
#################even value in list########
'''ele = [2, 3, 4, 5, 6, 7, 8]
for i in ele:
     if(i%2==0):
         print(i)'''

###########even index value in list#######
'''ele = [2, 3, 4, 5, 7, 6, 8]
for i in range(1,len(ele)):
    if i%2==0:
        print("Even index value",ele[i])'''
#########odd index value in list#########
'''ele = [2, 3, 4, 5, 6, 7, 8]
for i in range(0,len(ele)):
    if i%2==1:
        print("Odd index value",ele[i])'''
#########odd index value in reverse list#########
#ele = [2, 3, 4, 5, 6, 7, 8]
'''for i in range(len(ele),0):
    if i%2==1:
        print("Odd index value",ele[i])'''
'''ele = [2, 3, 4, 5, 6, 7, 8]
i=len(ele)
while(i>=0):
    if i%2==1:
        print("Odd index value",ele[i])

    i -=1
'''
#########Print vowel from the string in list:
str = "hello i am owlu"
l=[]
for i in str:
    if i=='a':
        l = i



print(l)

