'''a = 4
b= 2
try:
    c= a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your dividend is zero")'''
'''
a = 10
b =0
try:
    c=a/b
    print('C:',c)
except ZeroDivisionError as e:
    print("Exception:",e)'''

##########
'''name = input("Enter a charcter")
age = input("enter a age")
d = name+age
print(d)'''
#############
'''a = 4
b= 0
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your division is zero")
else: # it will be executed when no exception
    print("Your division was greater than zero")'''

###################
'''a =4
b= 0
try:
    c = a/b
    print('C:',c)
except ZeroDivisionError as e:
    print("Check your division is Zero",e)
finally:
    print("Always exected")'''
#####################
'''try:
    number = int(input("Enter a Number :"))
    if number > 10:
        raise Exception('invalid number')
except Exception as e:
    print(e)'''
##################
my_list = ['a','b','c']
try:
    print(my_list[4])
except IndexError as e:
    print("IndexError : ",e)
    